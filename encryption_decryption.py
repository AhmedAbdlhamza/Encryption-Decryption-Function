def encryption(string, step):
    encrypted_string = ""
    for char in string:
        if char.isalpha():
            encrypted_string += chr((ord(char) + step - 97) % 26 + 97)
        else:
            encrypted_string += char
    return encrypted_string

def decryption(encrypted_string, step):
    decrypted_string = ""
    for char in encrypted_string:
        if char.isalpha():
            decrypted_string += chr((ord(char) - step - 97) % 26 + 97)
        else:
            decrypted_string += char
    return decrypted_string


string = "hello world"
step = 2

encrypted_string = encryption(string, step)
print(f"Encrypted string: {encrypted_string}")

decrypted_string = decryption(encrypted_string, step)
print(f"Decrypted string: {decrypted_string}")

# Output:
# Encrypted string: jgnnq yqtnf
# Decrypted string: hello world
