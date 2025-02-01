import re

def check_password(pwd):
    def length_check(password):
        is_valid = False
        password_length = len(password)
        if 6 <= password_length <= 10:
            is_valid = True
        else:
            print('Password must be between 6 and 10 characters')
        return is_valid

    def symbols_check(password):
        is_valid = False
        if re.match(r'^[a-zA-Z0-9]+$', password):
            is_valid = True
        else:
            print("Password must consist only of letters and digits")
        return is_valid

    def last_symbols(password):
        is_valid = False
        if re.match(r'(?=(.*\d){2,})', password):
            is_valid = True
        else:
            print("Password must have at least 2 digits")
        return is_valid

    is_length = length_check(pwd)
    is_symbol = symbols_check(pwd)
    is_numbers = last_symbols(pwd)

    return is_length, is_symbol, is_numbers



input_password = input()

is_valid = all(check_password(input_password))

if is_valid:
    print('Password is valid')
