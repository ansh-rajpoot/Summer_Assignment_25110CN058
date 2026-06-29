def count_vowels_consonants(string_val):
    vowels = "aeiouAEIOU"
    vowels =0
    consonant= 0
    for char in string_val:
        if char.isalpha():
            if char in vowels:
                vowels += 1
            else:
                consonant +=1
                
    return vowels, consonant
user_str = input("Enter a string: ")

print("\nThe string you entered is:")
print(user_str)

v_result, c_result = count_vowels_consonants(user_str)
print("\nThe required vowel count is:-", v_result)
print("The required consonant count is:-", c_result)
