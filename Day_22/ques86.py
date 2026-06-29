# Write a program to Count words in a sentence.

def count_words(sentence):
    word_count = 0
    in_word =False


    
    for char in sentence:
        if char != ' ' and char != '\t' and char != '\n':
            if not in_word:
                word_count += 1
                in_word =True
        else:

            in_word= False         
    return word_count

user_str = input("Enter a sentence: ")

print("\nThe sentence you entered is:")
print(user_str)

print('\nThe number of words in given sentence is:-', count_words(user_str))
