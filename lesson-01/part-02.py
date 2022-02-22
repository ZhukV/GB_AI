from requests import request

username = input('Please enter a username on GitHub: ')
api_token = input('Please enter a api token on GitHub: ')


events_url = 'https://api.github.com/users/{username}/events'.format(username=username)
authorization = '{username}:{api_token}'.format(username=username, api_token=api_token)

response = request('GET', events_url, headers={
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': authorization
})

if response.status_code != 200:
    raise RuntimeError('Receive wrong status code {code}. Expect 200.'.format(code=response.status_code))


with open('result.json', 'w', encoding='utf-8') as f:
    f.write(response.text)
