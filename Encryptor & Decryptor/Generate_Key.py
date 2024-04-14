from cryptography.fernet import Fernet


key = Fernet.generate_key()
file = open("Encryptor & Decryptor\\Encryption_Key.txt", 'wb')
file.write(key)
file.close()