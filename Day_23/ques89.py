# Write a program to Find first non-repeating
# character.

def first_non_repeating_char(string_val):
    frequency_dict={}
    for char in string_val:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] =1
            
    for char in string_val:
        if frequency_dict[char] == 1:
            return char
    return None

user_str = input("Enter a string: ")
print()
print("The string you entered is:")
print(user_str)

result = first_non_repeating_char(user_str)
if result is not None:
    print("\nThe required first non-repeating character is:-", result)
else:
    print("\nThere are no non-repeating characters .")