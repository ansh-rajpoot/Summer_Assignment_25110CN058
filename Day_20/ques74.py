def subtract_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
            
    return result

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = []
print(f"\nPlease enter elements for Matrix 1 ({rows}x{cols}):")
for i in range(rows):
    row = []
    print(f"Row {i+1}:")
    for j in range(cols):
        element = int(input(f"  Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)

matrix2 = []
print(f"\nPlease enter elements for Matrix 2 ({rows}x{cols}):")
for i in range(rows):
    row = []
    print(f"Row {i+1}:")
    for j in range(cols):
        element = int(input(f"  Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix2.append(row)

print("\nMatrix 1 you entered is:")
print(matrix1)

print("\nMatrix 2 you entered is:")
print(matrix2)

print('\nThe required resultant matrix is:-', subtract_matrices(matrix1, matrix2))
