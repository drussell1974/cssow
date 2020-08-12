from cryptography.fernet import Fernet

def decrypt(key, file_name, ENC="UTF8"):
    ciphered_text = ""
    with open(file_name, 'r') as file_object:
        for line in file_object:
            ciphered_text = line

    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(bytes(ciphered_text, ENC))
    return plain_text.decode(ENC)