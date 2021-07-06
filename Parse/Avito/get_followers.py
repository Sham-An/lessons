import json
from pprint import pprint
import subprocess
import time
import urllib.parse


url_base = 'https://www.instagram.com/graphql/query/?'

command_template = """curl '{url}' -H 'pragma: no-cache' -H 'cookie: ds_user_id=5802924775; mid=Wlcy5QAEAAHjIpWdSStiUxb6Alq2; mcd=3; fbm_124024574287414=base_domain=.instagram.com; shbid=12189; ig_cb=1; datr=8RwpW26vPMlKFy71tY9xUaXL; csrftoken=ablLyNKzr5IEJDf96RKcb1JCLfvpmqKF; csrftoken=vHscIy3LQ3wFWnasxFramXjivISwDrB7; sessionid=5802924775%3AhVW56t3YGfTxF7%3A16; rur=VLL; shbts=1553170380.1821196; urlgen="{{\"89.17.61.234\": 201825\054 \"185.79.103.87\": 202173\054 \"176.59.45.101\": 12958}}:1h7243:G-7T5t74Otrp-GmJtQLHiBD_QeQ"' -H 'x-ig-app-id: 936619743392459' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-GB,en;q=0.9,en-US;q=0.8,ru;q=0.7' -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36' -H 'accept: */*' -H 'cache-control: no-cache' -H 'authority: www.instagram.com' -H 'x-requested-with: XMLHttpRequest' -H 'x-instagram-gis: f9aba92790c033ed04e6e2bb734236ba' -H 'referer: https://www.instagram.com/alexeygoloburdin/followers/' --compressed > json/followers_{index}.json"""

index = 1
after = None
followers_in_progress = 0
while True:
    after_value = f',"after":"{after}"' if after else ''
    variables = f'{{"id":"5802924775","include_reel":true,"fetch_mutual":false,"first":50{after_value}}}'
    get_params = {
        'query_hash': '56066f031e6239f35a904ac20c9f37d9',
        'variables': variables
    }
    ws_url = url_base + urllib.parse.urlencode(get_params)

    result = subprocess.run(command_template.format(url=ws_url, index=index), shell=True, capture_output=True)
    if result.returncode != 0:
        exit('Произошло зло, убиваемся')

    with open(f'json/followers_{index}.json', 'r') as f:
        data = json.load(f)

    if not data['data']['user']['edge_followed_by']['page_info']['has_next_page']:
        break

    after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']
    all_followers = data['data']['user']['edge_followed_by']['count']
    in_current_batch = len(data['data']['user']['edge_followed_by']['edges'])
    followers_in_progress += in_current_batch 
    print(f'Обработано {followers_in_progress}/{all_followers}')

    time.sleep(5 if index % 10 != 0 else 20)
    index += 1

print('#готоводело')
