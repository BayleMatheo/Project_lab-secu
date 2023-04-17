import requests


url = "http://51.15.136.118/userpage_cookie.php"
cookies = {'auth_id': 'value'}
r = requests.post(url, cookies=cookies)