import requests

url = input("Choose url: ")
with open('payloads.txt', 'r') as userfile:
    users = userfile.readlines()

for user in users:
    user = user.strip()
    passwd = "whatever"
    r = requests.post(url, data={'username': user, 'password': passwd})
    if "Nom d'utilisateur ou mot de passe incorrect" in r.text:
        print("No SQL injection vulnerability detected")
    else:
        print("Possible SQL injection vulnerability")
        print(user)

