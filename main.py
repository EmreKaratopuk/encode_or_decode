alphabet = "abcdefghijklmnopqrstuvwxyz"
new_alphabet = "ypoiwhslxvbuagmzcrqkfjnted"

while True:
    question = input("0 for exit, 1 for encoding, 2 for decoding \n")

    if question == "0":
        print("Goodbye")
        break

    elif question == "1":
        message = input("Please enter your message \n")
        new_message = ""
        for a in message:
            if a in alphabet:
                new_message += new_alphabet[alphabet.index(a)]
            elif a in alphabet.upper():
                new_message += new_alphabet.upper()[alphabet.upper().index(a)]
            else:
                new_message += a
        print("Your encrypted message is: " + new_message + "\n")

    elif question == "2":
        message = input("Please enter the encrypted message \n")
        new_message = ""
        for a in message:
            if a in new_alphabet:
                new_message += alphabet[new_alphabet.index(a)]
            elif a in new_alphabet.upper():
                new_message += alphabet.upper()[new_alphabet.upper().index(a)]
            else:
                new_message += a
        print("Your decrypted message is: " + new_message + "\n")
