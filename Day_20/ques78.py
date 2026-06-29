def is_symmetric(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
                
    return True

size = int(input("Enter   size of the square matrix (N x N): "))

matrix1 =[]
print(f"\nPlease enter elements for Matrix ({size}x{size}):")
for i in range(size):
    row = []
    print(f"Row {i+1}:")
    for j in range(size):
        element= int(input(f"  Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)

print("\nThe Matrix you entered :")
print(matrix1)

if is_symmetric(matrix1):
    print("\nThe matrix is symmetric.")
else:
    print("\nThe matrix is not symmetric.")
