import string
def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"

    # implement this
    res = []
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = [i for i in range(10)]
    for password in passwords:
        d =dict([('length', False), ('lowercase', False), ('uppercase', False), ('special_char', False), ('digit', False)])
        for char in password:
            if ord(char) >= 97 and ord(char) <= 122:
                d['lowercase'] = True
                break
        for char in password:
            if ord(char) >= 65 and ord(char) <= 90:
                d['uppercase'] = True
                break
        for char in password:
            if char in special_characters:
                d['special_char'] = True
                break
        for char in password:
            if char.isdigit():
                d['digit'] = True
        if len(password) >=8:
            d['length'] = True
        res.append(d)
    return res


def multi_password_strength_counter_1(passwords):
    special_characters = "!@#$%^&*()-+"

    # implement this
    res = []
    for password in passwords:
        strength = {
            'digit': any(char.isdigit() for char in password),
            'uppercase' : any(char.isupper() for char in password),
            'lowercase' : any(char.islower() for char in password),
            'special_char': any(char in special_characters for char in password),
            'length': len(password) >= 8
        }
        res.append(strength)
    return res

passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter_1(passwords)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}