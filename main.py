# Deepak Guggilam 10/25/2023
# Encode() function
def encode(password):
    encoded_password = ''
    for digit in password:
        digit = (int(digit) + 3) % 10
        encoded_password += str(digit)
    return encoded_password

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
            break
