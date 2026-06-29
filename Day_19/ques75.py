def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    result = [[0 for _ in range(rows)] for _ in range(cols)]  
    for i in range(rows):
        for j in range(cols):
            result[j][i]= matrix[i][j]          
    return result

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix1 =[]
print(f"\nPlease enter elements for Matrix ({rows}x{cols}):")
for i in range(rows):
    row= []
    print(f"Row {i+1}:")
    for j in range(cols):
        element =int(input(f"  Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)
print("\nThe Matrix you entered is:")
print(matrix1)
print('\nThe required transposed matrix is:-', transpose_matrix(matrix1))
