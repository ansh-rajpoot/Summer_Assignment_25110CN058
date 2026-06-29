# Write a program to Check palindrome string.

def is_palindrome(string_val):
    reversed_str =""
    for char in string_val:
        reversed_str= char + reversed_str
    if string_val == reversed_str:
        return True
    else:
        return False

user_str= input("Enter a string you want to check for palindrone: ")

print("\nThe string you entered is:")
print(user_str)

if is_palindrome(user_str):
    print("\nThe givenn string is a palindrome.")
else:
    print("\nThe given string is not a palindrome.")