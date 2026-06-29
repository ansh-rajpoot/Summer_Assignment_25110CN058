# Write a program to Find common characters
# in strings.

def find_common_characters(str1, str2):
    result =[]
    for char in str1:
        if char in str2 and char not in result:
            result.append(char)
            
    return "".join(result)

user_str1 = input("Enter the first string: ")
user_str2 = input("Enter the second string: ")

print("\nThe first string you entered is:")
print(user_str1)
print("The second string you entered is:")
print(user_str2)

print('\nThe required common characters are:-', find_common_characters(user_str1, user_str2))
