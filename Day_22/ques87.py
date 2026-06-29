# Write a program to Character frequency.

def character_frequency(string_val):
    frequency_dict={}
    for char in string_val:
        if char in frequency_dict:
            frequency_dict[char] +=1
        else:
            frequency_dict[char] = 1
            
    return frequency_dict

user_str = input("Enter the string: ")

print("\nThe string you entered is:")
print(user_str)
result =character_frequency(user_str)
print("\nThe required character frequency the given string has is:-")
for char in result:
    print(f"'{char}': {result[char]}")
