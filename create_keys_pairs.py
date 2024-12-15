import gnupg


gpg = gnupg.GPG(gnupghome="/tmp")
gpg.encoding = "utf-8"

encrypt_type = None
pass_phrase = input("Input a passphrase")
pass_phrase = input("Input an email")
options_map = {
                "1": "RSA",
                "2": "ECC",
                "3": "DH",
                "4": "ECDH",
                "5": "DSA",
                "6": "EdDSA",
            }
print("===== choose type encryptation =======\n")
options = """
1 - RSA 
2 - ECC
3 - DH
4 - ECDH
5 - DSA
6 - EdDSA
7 - exit
\n"""
print(options)
exit = False
while not exit:
    choose_type = input("Enter option type encrypt")
    if choose_type == "7":
        break
    try:
        encrypt_type = options_map[choose_type]
    except ValueError:
        print("Incorrect option")

