def reverse_string(string_val):
    reversed_str = ""
    for char in string_val:
# this is the one reversing the string as it is joining two string in the order that makes it reverse
        reversed_str = char + reversed_str
    return reversed_str





user_str = input("Enter a string: ")
print("\nThe string you entered is:")
print(user_str)




print('\nThe required reversed string is:-', reverse_string(user_str))
