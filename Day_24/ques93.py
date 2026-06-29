#  Write a program to Check string rotation.
def is_string_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
        
    combined_str =str1 + str1
    return str2 in combined_str

user_str1 = input("Enter the first string: ")
user_str2 = input("Enter the second string: ")



print("\nThe first string you entered is:")
print(user_str1)
print("The second string you entered is:")

print(user_str2)



if is_string_rotation(user_str1, user_str2):
    print("\nYES! The second string is a rotation of the first string.")
else:
    print("\nNO! The second string is not a rotation of the first string.")
