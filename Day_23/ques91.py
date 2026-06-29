# Write a program to Check anagram strings.




def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
        
    frequency = {}
    
    for char in str1:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    for char in str2:
        if char in frequency:
            frequency[char] -=1
        else:
            return False
            
    for count in frequency.values():
        if count != 0:
            return False
            
    return True

user_str1 =input("Enter the first string: ")
user_str2=input("Enter the second string: ")

print("\nThe first string you entered is:")
print(user_str1)
print("The second string you entered is:")
print(user_str2)




if is_anagram(user_str1, user_str2):
    print("\nThe strings are anagrams.")
else:
    print("\nThe strings are not anagrams.")
