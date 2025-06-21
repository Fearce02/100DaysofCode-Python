logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Enter your shift amount:\n"))



# def encrypt(original_text, shift_amount):
#         cipher_text = ""
#         for letter in original_text:
#             encrypted_word = alphabet.index(letter) + shift_amount

#             encrypted_word %= len(alphabet) #fix for the out of index error
#             cipher_text += alphabet[encrypted_word]
#         print(f"Here is the encoded result: {cipher_text}")



# def decrypt(encryptcode, shiftamount):
#     decrypt_word = ""
#     for letter in encryptcode:
#         decrypted_code = alphabet.index(letter) - shiftamount

#         decrypted_code %= len(alphabet)
#         decrypt_word += alphabet[decrypted_code]
#     print(f"This is the decoded result: {decrypt_word}") 


# if direction == 'encode':
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     encrypt(original_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decode_text = input("Type your message to decode: de").lower()
#     shift = int(input("Type the shift number:\n"))
#     decrypt(encryptcode=decode_text, shiftamount=shift)


def caesar(original_text, shift_amount, directionality):
    decrypt_word = ""
    for letter in original_text:

        if directionality == 'decode':
            decrypted_code = alphabet.index(letter) - shift_amount
        elif directionality == 'encode':
            decrypted_code = alphabet.index(letter) + shift_amount

        decrypted_code %= len(alphabet)
        decrypt_word += alphabet[decrypted_code]

    if directionality == 'encode':
        print(f"This is the encoded result: {decrypt_word}")
    elif directionality == 'decode':
        print(f"This is the decoded result: {decrypt_word}")
    

caesar(original_text=text, shift_amount=shift, directionality=direction)


