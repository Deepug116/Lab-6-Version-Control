# Deepak Guggilam 10/25/2023
# Encode() function
def encode(password):
    encoded_password = ''
    for digit in password:
        digit = (int(digit) + 3) % 10
        encoded_password += str(digit)
    return encoded_password

# Annalisa Folsom 10/25/2023
# Decode() function
def decode(encoded_password):
    dec_list = list(encoded_password)  # Changes the str to a list.
    index = 0
    index_1 = 0
    for element in dec_list:  # Changes str to int.
        dec_list[index] = int(element)
        index += 1
    for element in range(len(dec_list)):  # Subtract 3 from each digit...if negative, add 10
        dec_list[index_1] = dec_list[index_1] - 3
        if dec_list[index_1] < 0:
            dec_list[index_1] += 10
        index_1 += 1
    decoded_password = "".join(map(str, dec_list))  # This line structure is based on Deepak's commit to Annalisa's repo

    return decoded_password

if __name__ == '__main__':
    password = None
    encoded_password = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Quit")
        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            password = input("Please enter your password to encode:")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        elif user_input == 2:
            if encoded_password is not None:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            else:
                print("You need to encode a password first.\n")

        elif user_input == 3:
            break
