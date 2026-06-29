# Write a program to Sort words by length.

def sort_words_by_length(words_list):
    n =len(words_list)
 
    for i in range(n - 1):
        min_index= i
 
        for j in range(i + 1, n):
            if len(words_list[j]) < len(words_list[min_index]):
                min_index = j
                
        words_list[i], words_list[min_index] = words_list[min_index], words_list[i]
        
    return words_list

size =int(input("Enter the number of words you want to enter  : "))
arr1 =[]
 
print(f"Please enter {size} words:")
for i in range(size):
    word = input(f"Word {i+1}: ")
    arr1.append(word)

print("\nThe complete list of words you entereed is:")
print(arr1)


print('the required sorted array is:-', sort_words_by_length(arr1))
