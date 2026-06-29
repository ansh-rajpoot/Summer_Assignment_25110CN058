# Write a program to Remove spaces from string.

def remove_spaces(string_val):
    result=""
    for char in string_val:
        if char != ' ' and char != '\t' and char != '\n':
            result +=char
    return result




user_str = input("Enter a string: ")

print("\nThe string you entered is:")
print(user_str)
print('\nThe string without spaces is:-', remove_spaces(user_str))
