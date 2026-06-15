# write a program to rotate an array right
def reverse_sub_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_right(arr, d):
    n = len(arr)
    if n == 0:
        return arr
        
    d = d % n 
    reverse_sub_array(arr, 0, n - 1)

    reverse_sub_array(arr, 0, d - 1)

    reverse_sub_array(arr, d, n - 1)
    
    return arr

arr=[]
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
target=int(input('Enter how many index you wanna rotate: '))
result=rotate_right(arr,target)
print('The required rotated array is', result)