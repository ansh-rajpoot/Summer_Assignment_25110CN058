# Function to find the maximum frequency element
def find_max_frequency_element(arr):
    if not arr:
        return None, 0
        
    frequency_map = {}
    for element in arr:
        if element in frequency_map:
            frequency_map[element] += 1
        else:
            frequency_map[element] = 1
            
    max_element = arr[0]
    max_count = 0
    
    for element, count in frequency_map.items():
        if count > max_count:
            max_count = count
            max_element = element
            
    return max_element, max_count
arr = []
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)

most_frequent, frequency = find_max_frequency_element(arr)

print(f"\nThe maximum frequency element is {most_frequent} (appears {frequency} times).")
