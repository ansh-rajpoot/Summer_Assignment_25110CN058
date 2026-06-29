# Write a program to Remove duplicate
# characters.

def remove_duplicates_easy(string_val):
    result = ""
    
    for char in string_val:
        if char not in result:
            result += char
    return result

user_str =input("Enter a string: ")

print("\nThe string you entered is:")
print(user_str)



print('\nThe required string without duplicates is:-', remove_duplicates_easy(user_str))
