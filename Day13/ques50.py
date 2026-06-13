# Q50 Write a program to Find sum and average of array.
arr=[]
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)

sum=0

for i in arr:
    sum+=i
print('The sum of given array is', sum)
avg= sum/size
print('The average of given array is', avg)

