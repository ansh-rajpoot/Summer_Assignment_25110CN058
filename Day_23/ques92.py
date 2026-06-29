# Write a program to Find maximum occurring character.
def max_occurring_char(string_val):
    if not string_val:
        return None
    frequency_dict={}
    for char in string_val:
        if char in frequency_dict:
            frequency_dict[char] +=1
        else:
            frequency_dict[char] = 1
            

            
    max_char = string_val[0]
    max_count = frequency_dict[max_char]
    
    for char in frequency_dict:
        if frequency_dict[char] > max_count:
            max_count = frequency_dict[char]
            max_char = char
            
    return max_char

user_str = input("Enter string: ")

print("\nThe string entered is:")
print(user_str)


result = max_occurring_char(user_str)
if result is not None:
    print("\nThe required maximum occurring character:-", result)
else:
    print("\nThe string you entered is empty.")
