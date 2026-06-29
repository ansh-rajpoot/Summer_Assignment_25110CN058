# write a program to bubble sort
def bubble_sort(arr):
    
    for j in range(len(arr)):
        swapped=False
        for i in range(len(arr)-1-j):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped=True
        if not swapped:
            break
        
    return arr
# array=[5,4,3,2]
# print(bubble_sort(arr=array))
arr1 = []
size = int(input("Enter the number of elements you want in the array 1: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr1.append(element)

print("\nThe complete array 1 you entered is:")
print(arr1)
print('the required sorted array is:-', bubble_sort(arr1))
