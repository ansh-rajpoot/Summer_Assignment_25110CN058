# Write a program to Sort names
# alphabetically.

def sort_names_alphabetically(names_list):
    n = len(names_list)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if names_list[j] < names_list[min_index]:
                min_index = j           
        names_list[i], names_list[min_index] = names_list[min_index], names_list[i]
        
    return names_list

size =int(input("Enter the number of names you want to enter: "))
arr1= []
 
print(f"Please enter {size} names:")
for i in range(size):
    name = input(f"Name {i+1}: ")
    arr1.append(name)
print("\nThe complete list of names you entered is:")
print(arr1)


print('the required sorted array is:-', sort_names_alphabetically(arr1))
