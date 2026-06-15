# Write a program to reverse an array

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1        
    return arr

my_list = [1, 2, 3, 4, 5]
print(reverse_array(my_list))   

arr=[]
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
 
result= reverse_array(arr)
print('The reversed array is',result)