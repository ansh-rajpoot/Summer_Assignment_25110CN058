# Q54 write a program to frequency of an element
def find_frequency(arr, target):
    count = 0
    # Loop through each item in the list
    for item in arr:
        if item == target:
            count += 1  # Increment counter if matched
    return count

arr=[]
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
target_val= int(input('Enter the target value:- '))
result=find_frequency(arr,target_val)
print('The frequency of the given target value is',result)