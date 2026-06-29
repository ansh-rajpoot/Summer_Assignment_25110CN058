def diagonal_sum(matrix):
    n = len(matrix)
    total_sum= 0
    
    for i in range(n):
        total_sum += matrix[i][i]
        
    return total_sum

size =int(input("Enter the size of the square matrix (N x N): "))
matrix1= []
print(f"\nPlease enter elements for Matrix ({size}x{size}):")
for i in range(size):
    row = []
    print(f"Row {i+1}:")
    for j in range(size):
        element = int(input(f"  Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)
print("\nThe Matrix you entered is:")
print(matrix1)
print('\nThe required diagonal sum is:-', diagonal_sum(matrix1))
