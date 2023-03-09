import random
import string

# These special char can be chosen for passwords
special_char = "!@/()=-"

# Gives the amount one char type has to be in the password at least
rep = 4

# Create the defined amount of specific characters
special_char_list = [random.choice(special_char) for special in range(rep)]
digit_char_list = [random.choice(string.digits) for digit in range(rep)]
lower_char_list = [random.choice(string.ascii_lowercase) for lower in range(rep)]
upper_char_list = [random.choice(string.ascii_uppercase) for upper in range(rep)]

# Combine the defined lists together
defined_password_list = special_char_list + digit_char_list + lower_char_list + upper_char_list

# Gives the amount of addition chars to add to the password list
pass_length = 10

# Extents the password list, with the pass_length parameter
password_extension = [random.choice(string.ascii_lowercase + string.ascii_uppercase + special_char + string.digits)
                      for i in range(pass_length)]

# Combines the tow password lists
password_list = defined_password_list + password_extension
print(password_list)

# Randomizes the order of the chars of the list
random.shuffle(password_list)
print(password_list)

# Concatenates the chars from the list to a string with a separator of ''
password = ''.join(password_list)
print(password)
print(len(password))

