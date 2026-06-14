# Q56 Write a program to find duplicates in array
def find_duplicates(arr):
    n = len(arr)
    duplicates = []
    for i in range(0, n):

        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                already_added = False
                for x in duplicates:
                    if x == arr[i]:
                        already_added = True
                        break
                if not already_added:
                    duplicates.append(arr[i])
                    
    return duplicates

arr=[]
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
 
result=find_duplicates(arr)
print('The duplicates in the given array are',result)