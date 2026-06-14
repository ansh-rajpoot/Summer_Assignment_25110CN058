# Q53 Write a program to linear search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   

arr=[]
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
target= int(input('Enter the target value:- '))

result=linear_search(arr,target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print('Element not found!')