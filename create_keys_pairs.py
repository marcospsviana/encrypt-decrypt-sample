import gnupg


gpg = gnupg.GPG(gnupghome="/tmp")
gpg.encoding = "utf-8"

pass_phrase = input("Input a passphrase")
pass_phrase = input("Input a passphrase")

