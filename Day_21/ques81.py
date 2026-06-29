def find_string_length(string_val):
    count = 0
    for char in string_val:
        count +=1
    return count

given_str =input("Enter a string: ")

print("\nThe string you entered is:")
print(given_str)
print('\nThe  given string length is:-', find_string_length(given_str))
