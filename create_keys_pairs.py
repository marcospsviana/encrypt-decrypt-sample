import gnupg


gpg = gnupg.GPG(gnupghome="/tmp")
gpg.encoding = "utf-8"


def make_keys():
    input_data = gpg.gen_key_input(
                    name_real='name',
                    name_email='name@email.com',
                    passphrase='passphrase',
                    key_type='RSA',
                    key_length =2048,
                    expire_date='2y'
                )
    gpg.gen_key(input_data)


make_keys()