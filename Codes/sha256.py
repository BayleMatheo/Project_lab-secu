import hashlib

# Hash to crack
hash_to_crack = "42918bcc531588a6ba0387bc1ddc30176c08c390532074a8685f118bdea05a48" # this is the SHA-256 hash of the word "password"

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