import string
import keyword

user_input = input("Введіть ім'я змінної: ")

is_valid = (
    user_input and
    not user_input[0].isdigit() and
    user_input.islower() and
    user_input.count('_') <= 1 and
    user_input not in keyword.kwlist and
    all(char in string.ascii_lowercase + string.digits + '_' for char in user_input)
)

print(is_valid)