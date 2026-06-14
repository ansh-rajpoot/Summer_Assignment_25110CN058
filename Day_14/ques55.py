# Q55 Write a program to second largest element
def find_second_largest_elements(arr):
    n = len(arr)
    if n < 2:
        return "Invalid Input"
    if arr[0] > arr[1]:
        largest = arr[0]
        second_largest = arr[1]
    else:
        largest = arr[1]
        second_largest = arr[0]
        
    for i in range(2, n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
        elif largest == second_largest and arr[i] < largest:
            second_largest = arr[i]

    if largest == second_largest:
        return "No unique second largest element exists"
        
    return second_largest


arr=[]
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
result=find_second_largest_elements(arr)
print('The second largest element is', result)