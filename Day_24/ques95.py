# Write a program to Find longest word.
def find_longest_word(sentence):
    longest_word = ""
    current_word=""
    
    for char in sentence:


        if char !=' ' and char != '\t' and char != '\n' and char != '.' and char != ',' and char != '!' and char != '?':
            current_word += char
        else:

            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ""



    if len(current_word) > len(longest_word):
        longest_word = current_word
    return longest_word

user_str = input("Enter a sentence: ")

print("\nThe sentence you entered is:")
print(user_str)



print('\nThe required longest word is:-', find_longest_word(user_str))
