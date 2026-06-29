# Write a program to Find first repeating character.

def first_repeating_char(string_val):
    seen_set = set()
    
    for char in string_val:
        if char in seen_set:
            return char
        seen_set.add(char)

        
        
    return None

user_str =input("Enter  string: ")
print("\nThe string entered is:")
print(user_str)


result = first_repeating_char(user_str)
if result is not None:
    print("\nThe required first repeating character is:-", result)
else:
    print("\nThere are no repeating characters.")
