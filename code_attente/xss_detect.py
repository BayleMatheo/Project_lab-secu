import requests

# Liste de pages à tester
pages = ["https://www.mon-site-web.com/page1.html",
         "https://www.mon-site-web.com/page2.html",
         "https://www.mon-site-web.com/page3.html"]

# Caractères spécifiques pour détecter une vulnérabilité XSS
xss_chars = ["<script>", "alert(", "onload="]

# Parcourir chaque page et envoyer une requête GET
for page in pages:
    response = requests.get(page)
    # Vérifier si les caractères spécifiques sont présents dans la réponse
    for char in xss_chars:
        if char in response.text:
            print(f"La page {page} est vulnérable aux failles XSS.")