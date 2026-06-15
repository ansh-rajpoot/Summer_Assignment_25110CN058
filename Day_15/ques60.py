# write a program to move zeroes to end
def move_zeroes_to_end(arr):
    non_zeroes = [x for x in arr if x != 0]
    zeroes = [x for x in arr if x == 0]
    return non_zeroes + zeroes

arr=[]
size =int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element =int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)

result=move_zeroes_to_end(arr)
print('The required  array is', result)