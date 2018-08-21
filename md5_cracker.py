import hashlib

salts = [
    "6MAp84",
    "bQkChe",
    "HnqeN4",
    "e5ad5s",
    "g9Wxv7",
    "HCCsxP",
    "cC5nTr",
    "h8spZR",
    "tb9AWe"
]
passkeys = [
    "c2d8960157fc8540f6d5d66594e165e0",
    "727a279d913fba677c490102b135e51e",
    "8c3c3152a5c64ffb683d78efc3520114",
    "6ba94d6322f53f30aca4f34960203703",
    "c789ec9fae1cd07adfc02930a39486a1",
    "fec21f5c7dcf8e5e54537cfda92df5fe",
    "6a113db1fd25c5501ec3a5936d817c29",
    "7db5040c351237e8332bfbba757a1019",
    "dd272382909a4f51163c77da6356cc6f"
]
lines = filter(None, (line.rstrip() for line in open("/usr/share/wordlists/rockyou.txt", encoding='iso-8859-1')))  # Remove the empty lines
for password in lines:
    password = password.encode('iso-8859-1')  # Encoding is required for hashing
    for arrays_index in range(0, len(salts)):
        salt = salts[arrays_index].encode('iso-8859-1')
        pass_md5 = hashlib.md5(password).hexdigest().encode('iso-8859-1')  # First MD5 hash for the password
        word_md5 = hashlib.md5(pass_md5+salt).hexdigest()  # Second MD5 hash with the salt
        if word_md5 == passkeys[arrays_index]:
            print("The password is {} for passkey {}".format(password.decode("utf-8"), passkeys[arrays_index]))
print("Done!!")
