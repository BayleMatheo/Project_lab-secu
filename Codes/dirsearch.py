import requests

r = requests.Session()

url = 'http://51.15.136.118/'

with open('./wordlists/dirlist.txt', 'r') as dirfile:
    hidedir = dirfile.readlines()

list_dir = []

for i in hidedir:
    hidedir = i.strip()
    fullurl = url+hidedir
    a = r.post(fullurl)
    if a.status_code != 404:
        list_dir.append(i)

string = []
for line in list_dir:
    string.append(line.replace("\n", ""))

print(str(string))
