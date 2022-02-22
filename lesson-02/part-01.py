from typing import Iterator
from requests import request
from urllib.parse import quote as url_quote
from bs4 import BeautifulSoup
import pandas as pd
import re


class ResultItem:
    title: str
    min_price: float
    max_price: float
    link: str
    source: str

    def __init__(self, title: str, min_price: float, max_price: float, link: str, source: str):
        self.title = title
        self.min_price = min_price
        self.max_price = max_price
        self.link = link
        self.source = source

    def data_for_pandas(self):
        return [self.title, self.min_price, self.max_price, self.link, self.source]

    @staticmethod
    def headers():
        return ['Title', 'Min price', 'Max price', 'Link', 'Source']


def convert_to_rub(currency: str, amount: float) -> float:
    if currency == 'USD':
        return amount * 80

    if currency == 'RUB' or currency == 'руб':
        return amount

    if currency == 'UAH' or currency == 'грн':
        return amount * 27

    raise ValueError('Unknown currency {currency}'.format(currency=currency))


def parse_compensation(compensation: str):
    r = re.search(r'(\d+(\s\d+)?)\s.\s(\d+(\s\d+)?)\s(USD|RUB|руб|грн)\.?', compensation)

    if r:
        min_amount = float(re.sub(r'\s+', '', r[1]))
        max_amount = float(re.sub(r'\s+', '', r[3]))

        min_amount = convert_to_rub(r[5], min_amount)
        max_amount = convert_to_rub(r[5], max_amount)

        return min_amount, max_amount

    r = re.search(r'(\d+(\s\d+)?)\s(USD|RUB|руб|грн)\.?', compensation)

    if r:
        min_amount = float(re.sub(r'\s+', '', r[1]))
        min_amount = convert_to_rub(r[3], min_amount)

        return min_amount, min_amount

    raise ValueError('Can\'t parse compensation from "{str}".'.format(str=compensation))


def parse_page_from_hh(query: str, page: int = 1) -> Iterator[ResultItem]:
    url = 'https://hh.ru/search/vacancy?text={query}&page={page}'.format(query=url_quote(query), page=page - 1)

    response = request('GET', url, headers={
        'accept': 'text/html, */*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    })

    if response.status_code != 200:
        raise RuntimeError('Receive wrong status code from HH "{code}"'.format(code=response.status_code))

    bs = BeautifulSoup(response.content, features='lxml')

    items = bs.select('.vacancy-serp-item')

    for item in items:
        item_name_block = item.select_one('.resume-search-item__name a')
        link = item_name_block.get('href')
        title = item_name_block.text

        compensation_block = item.select_one('[data-qa="vacancy-serp__vacancy-compensation"]')

        if compensation_block:
            min_price, max_price = parse_compensation(compensation_block.text)
        else:
            min_price = max_price = None

        yield ResultItem(title=title, min_price=min_price, max_price=max_price, link=link, source='hh')


def parse_from_hh(query: str, pages: int) -> Iterator[ResultItem]:
    for page in range(1, pages + 1):
        parse_items = parse_page_from_hh(query, page)

        for parse_item in parse_items:
            yield parse_item


def collect_items_to_pandas(elements: Iterator[ResultItem]) -> pd.DataFrame:
    data = []

    for element in elements:
        data.append(element.data_for_pandas())

    return pd.DataFrame(data, columns=ResultItem.headers())


query = input('Please enter a query for search Job: ')
pages = int(input('Please enter a count pages for parse: '))

elements = parse_from_hh(query, pages)

pd = collect_items_to_pandas(elements)

pd.to_csv('result.csv', index=False)
