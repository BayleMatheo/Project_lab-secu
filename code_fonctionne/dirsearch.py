import requests

r = requests.Session()

url = 'http://51.15.136.118:80/'

with open('dirlist.txt', 'r') as dirfile:
    hidedir = dirfile.readlines()

list_dir = []

for i in hidedir:
    hidedir = i.strip()
    fullurl = url+hidedir
    print(fullurl)
    a = r.post(fullurl)
    if a.status_code != 404:
        list_dir.append(i)

string = []
for newline in list_dir:
    string.append(newline.replace("\n", ""))

print(str(string))
