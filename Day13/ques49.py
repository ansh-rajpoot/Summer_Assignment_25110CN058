# Q49 Write a program to Input and display array.

array = []

 
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = input(f"Element {i+1}: ")
    array.append(element)

 
print("\nThe complete array is:")
print(array)

 
print("\nDisplaying elements individually:")
for item in array:
    print(item)