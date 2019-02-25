#-------------------- Proses Sign Up, Sign In & Enkripsi dengan Caesar Cipher --------------------

# Proses enkripsi password
def encrypt(password,shift): 
    encryptPassword = "" 

    for i in range(len(password)): 
        char = password[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            encryptPassword += chr((ord(char) + shift - 65) % 26 + 65) 
        # Encrypt lowercase characters 
        else: 
            encryptPassword += chr((ord(char) + shift - 97) % 26 + 97) 
  
    return encryptPassword
