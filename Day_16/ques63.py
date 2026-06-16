# write a program to find pair with given sum
def find_pair(arr, target):
    seen = set()
    for num in arr:
        complement =target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)    
    return None


arr = []
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
target=int(input('Enter the target sum:- '))
print('The required pairs are', find_pair(arr,target))