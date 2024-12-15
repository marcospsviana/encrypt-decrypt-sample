import gnupg

gpg = gnupg.GPG(gnupghome="/tmp")

with open("public.pem", "rb") as file:
    results = gpg.import_keys(file.read())
    if results.counts == 0:
        raise ImportError("Fail to import public key")
public_key = gpg.list_keys()
fingerprint = public_key.fingerprints

    

def encrypt_file(file_path, output_file):
    try:
        with open(file_path, "rb") as f:
            status = gpg.encrypt_file(f, recipients=fingerprint, output=output_file)
            if status.ok:
                print(f"File {file_path} encrypted successfull")
            else:
                print(f"Fail to ecrypt file: {status.stderr}")
                raise
    except Exception as err:
        raise f"Exception error to try encrypt file: {err}"
        

