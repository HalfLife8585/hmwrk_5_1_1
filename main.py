import keyword

user_input = input("Введіть ім'я змінної: ")

valid = (
    user_input and
    not user_input[0].isdigit() and
    user_input.islower() and
    user_input.count('_') <= 1 and
    all(char.isalnum() or char == '_' for char in user_input) and
    user_input not in keyword.kwlist
)

print(valid)