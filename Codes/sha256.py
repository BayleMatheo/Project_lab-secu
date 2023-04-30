import hashlib

# Hash to crack
hash_to_crack = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918" # this is the SHA-256 hash of the word "password"

# Read dictionary file
with open('./wordlists/password256.txt', "r") as file:
    for line in file:
        word = line.strip()
        # Hash the word
        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        # Compare the hash
        if hashed_word == hash_to_crack:
            print("Password found: " + word)
            break
    else:
        print("Password not found in dictionary.")