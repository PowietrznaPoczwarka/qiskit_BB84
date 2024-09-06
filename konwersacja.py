import os

def text_to_binary(text):
    binary_representation = ''.join(format(ord(char), '08b') for char in text)
    return binary_representation

def binary_to_text(binary_string):
    binary_values = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    text_characters = ''.join(chr(int(binary, 2)) for binary in binary_values)
    return text_characters

def encode_message(message, key):
    repeated_key = key * (len(message) // len(key)) + key[:len(message) % len(key)] # w przypadku gdy zakodowana wiadomosc jest dluzsza niz klucz, to zapetlamy klucz
    encoded_message = ''
    for i in range(len(message)):
        encoded_bit = str(int(message[i]) ^ int(repeated_key[i]))
        encoded_message += encoded_bit
    return encoded_message

def decode_message(encoded_message, key):
    repeated_key = key * (len(encoded_message) // len(key)) + key[:len(encoded_message) % len(key)] # w przypadku gdy zakodowana wiadomosc jest dluzsza niz klucz, to zapetlamy klucz
    decoded_message = ''
    for i in range(len(encoded_message)):
        decoded_bit = str(int(encoded_message[i]) ^ int(repeated_key[i]))
        decoded_message += decoded_bit
    return decoded_message

text = "Pozdrawiam Pana Sebastiana"

binary_text = text_to_binary(text)
#print(binary_text)

alice_encryption_key = os.environ.get('KLUCZ ALICE')
print(alice_encryption_key)
encoded_binary = encode_message(binary_text, alice_encryption_key)
print("wiadomość wysłana do Boba: \n", encoded_binary) #Wysyłanie do Boba

bob_encryption_key = os.environ.get('KLUCZ BOB')
print(bob_encryption_key)
decoded_binary = decode_message(encoded_binary, bob_encryption_key)
returned_text = binary_to_text(decoded_binary)

print(f"\n Wiadomość odkodowana przez Boba:\t {returned_text} \n")