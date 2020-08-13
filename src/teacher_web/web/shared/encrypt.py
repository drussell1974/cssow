# encrypt
from cryptography.fernet import Fernet
from decrypt import decrypt
ENC="UTF8"

def encrypt():
    # Enter password

    print("enter password which must be converted to bytes...")
    server_name = input("Database Server: ")
    database_name = input("Database name: ")
    password = input("Enter a password: ")
    password_in_bytes = bytes(password, ENC)

    file_name = "db.{}.{}.bin".format(server_name, database_name)

    # Create key
    print("\ngenerating key...")
    key = Fernet.generate_key()
    # write key to file
    print("\ncopy-and-paste the public key to the configuation file:\n", key.decode(ENC))

    # encrypt password
    print("\ngenerating ciphered text...")
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(password_in_bytes)   #required to be bytes

    with open(file_name, 'wb') as file_object:
        file_object.write(ciphered_text)
    print("\nupload private key file to server:\n", file_name)

    # verify 
    unciphered_text = decrypt(key, file_name, ENC)
    assert unciphered_text == password
    print("\nverified")

encrypt()