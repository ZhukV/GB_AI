from requests import request

response = request('GET', 'https://api.github.com/orgs/FiveLab/repos', headers={
    'Accept': 'application/vnd.github.v3+json'
})

if response.status_code != 200:
    raise RuntimeError('Receive wrong status code {code}. Expect 200.'.format(code=response.status_code))

with open('result.json', 'w', encoding='utf-8') as f:
    f.write(response.text)
