import base64

encoded_string = "YWRtaW52NGVyOWVzZGZ2ZQ"
decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8')
print(decoded_string)