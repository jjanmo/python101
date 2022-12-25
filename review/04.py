from requests import get

websites = (
    'google.com',
    'naver.com',
    'daum.net',
    'github.com'
)

results = {}

for site in websites:
    if not site.startswith('https://'):
        site = f'https://{site}'

    response = get(site)
    if response.status_code == 200:
        results[site] = 'OK'
    else:
        results[site] = "FAILED"
