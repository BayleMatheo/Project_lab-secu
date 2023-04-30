import requests

r = requests.Session()

url = 'http://51.15.136.118/'

with open('./wordlists/dirlist.txt', 'r') as dirfile:
    hidedir = dirfile.readlines()

list_dir = []

for i in hidedir:
    hidedir = i.strip()
    fullurl = url+hidedir
    # print(fullurl)
    a = r.post(fullurl)
    if a.status_code != 404:
        list_dir.append(i)
    print(list_dir)

string = []
for newline in list_dir:
    string.append(newline.replace("\n", ""))

print(str(string))
