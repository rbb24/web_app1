from getpass import getpass

lower, upper, digit, special = 0, 0, 0, 0
password_min_length = 10
password_max_length = 20
special_chars = "!@/()=-"
minimum = 2

print(f"""
Please enter a password.
The password needs a length between 12 and 20 chars
It has to include at least 2 special character, which are: {special_chars}
It has to include at least 2 digits
It has to include at least 2 lowercase letters
And it has to include at least 2 uppercase letters
""")

password = getpass()
check_password = getpass("Repeat password please: ")

# compare passwords
if password == check_password:
    print("The passwords are the same. You did good!")

    # check if password has the correct length
    if password_min_length <= len(password) <= password_max_length:
        print("The password has the right length")
        for char in password:

            # count lowercase letters
            if char.islower():
                lower += 1

            # count uppercase letters
            if char.isupper():
                upper += 1
            # count digits
            if char.isdigit():
                digit += 1

            # count special characters
            if char in special_chars:
                special += 1

    # check if requirements are met, and no not allowed special char was given
    if lower >= minimum and upper >= minimum and digit >= minimum and special >= minimum \
            and lower + upper + digit + special == len(password):
        print("Valid password")
    test = True
    while test:
        if lower < minimum:
            print(f"Not enough lowercase letters. Given {lower}, required {minimum}")
        if upper < minimum:
            print(f"Not enough uppercase letters. Given {upper}, required {minimum}")
        if digit < minimum:
            print(f"Not enough digits. Given {digit}, required {minimum}")
        if special < minimum:
            print(f"Not enough special characters from this list {special_chars} Given {special}, required {minimum}")
        if not lower+upper+digit+special == len(password):
            print(f"Not allowed special character was given. Allowed are only {special_chars}")
        test = False

    else:
        print("Not a valid password")

else:
    print("Passwords are not the same. Run the program again.")
