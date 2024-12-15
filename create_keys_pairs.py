import gnupg


gpg = gnupg.GPG(gnupghome="/tmp")
gpg.encoding = "utf-8"


def generate_keys_pair():
    input_data = gpg.gen_key_input(
                    name_real='name',
                    name_email='name@email.com',
                    passphrase='passphrase',
                    key_type='RSA',
                    key_length =2048,
                    expire_date='2y'
                )
    gpg.gen_key(input_data)
    key_ids = [g["keyid"] for g in gpg.list_keys(True)]
    gpg.export_keys(keyids=key_ids, secret=True, passphrase="passphrase", output="private.pem")
    gpg.export_keys(keyids=key_ids,  passphrase="passphrase", output="public.pem")
    
    


generate_keys_pair()