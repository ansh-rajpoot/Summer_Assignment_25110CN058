# write a program to find missing number in an array
def find_missing(arr):
    n=len(arr)+1
    expected_sum=n*(n+1)/2
    real_sum=sum(arr)
    return expected_sum-real_sum

arr=[]
size =int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element =int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)

print('The missing number is', find_missing(arr))
