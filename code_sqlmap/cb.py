tab = ["id", "username", "password"]
nom_colonne = ["1","2","3","4"]
idk = ['xyz', 'test', 'moi', 'admin', '1678', '234', '768', '598']

a=idk[:4]
b=idk[4:]
"""
print(" {} {} ".format(tab[0], nom_colonne))
print(" {} {} ".format(tab[1], a))
print(" {} {} ".format(tab[2], b))"""

for i in range(len(tab)):
    for j in range (len(nom_colonne)):
        print(nom_colonne[j] + tab[i])