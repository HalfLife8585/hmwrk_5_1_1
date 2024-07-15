import keyword

def is_valid_variable_name(name):
    if not name or name[0].isdigit():
        return False
    for char in name:
        if char.isupper() or char in ", .!?;:/\'\"\t\n\r":
            if char == "_":
                continue
            return False
    if keyword.iskeyword(name) or len(name.replace("_", "")) > 1:
        return False
    return True

name = input("Введіть ім'я змінної: ")
print("True" if is_valid_variable_name(name) else "False")
