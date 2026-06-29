def convert_to_uppercase(string_val):
    result= ""
    for char in string_val:
        if 'a' <= char <= 'z':
            result +=chr(ord(char) - 32)
        else:
            result +=char
    return result

user_str = input("Enter a string: ")
print("\nThe string you entered is:-")
print(user_str)



print('\nThe required uppercase string is:', convert_to_uppercase(user_str))
