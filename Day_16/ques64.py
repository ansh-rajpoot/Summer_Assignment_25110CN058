# write a program to remove duplicates from a array
def remove_duplicates_ordered(arr):
    seen = set()
    unique_arr = []
    for num in arr:
        if num not in seen:
            unique_arr.append(num)
            seen.add(num) 
    return unique_arr


arr = []
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
print('The required arrray without duplicates is', remove_duplicates_ordered(arr))