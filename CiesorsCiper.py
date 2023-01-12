# import math
# print(math.ceil(19.5))
import art
import letters

print(art.logo)
continue_work = True
while continue_work:
    choice = input("Type 'encode' to encrypt and 'decode' to decrypt : ")
    if choice == "encode":
        msg = input("Type your message : ").lower()
        shift = int(input("Type the shift number : "))
        new_msg = ""
        for l in msg:
            if l in letters.alphabet:
                pos = (letters.alphabet.index(l) + shift) % 52
                new_msg = new_msg + letters.alphabet[pos]
            else:
                new_msg = new_msg + l
        print("Here's the encoded result : " + new_msg)
    elif choice == "decode":
        msg = input("Type your message : ").lower()
        shift = int(input("Type the shift number : "))
        new_msg = ""
        for l in msg:
            if l in letters.alphabet:
                pos = (letters.alphabet.index(l) - shift) % 52
                new_msg = new_msg + letters.alphabet[pos]
            else:
                new_msg = new_msg + l
        print("Here's the decoded result : " + new_msg)
    else:
        print("Wrong option selected. Please try again")
    option = input("Type 'yes' if you want to go again. Otherwise type 'no' : ").lower()
    if option == "no":
        print("Thank you")
        continue_work = False
    elif option == "yes":
        continue
    else:
        print("Wrong option selected. Please try again")
