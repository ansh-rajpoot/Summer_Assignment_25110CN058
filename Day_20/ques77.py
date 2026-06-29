def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])
    
    result =[[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
    return result

rows1= int(input("Enter rows for Matrix 1: "))
cols1 = int(input("Enter columns for Matrix 1: "))

rows2 = int(input("Enter rows for Matrix 2: "))
cols2 =int(input("Enter columns for Matrix 2: "))

if cols1 != rows2:
    print("\nError: Multiplication not possible! Columns of Matrix 1 must equal Rows of Matrix 2.")
else:
    matrix1 = []
    print(f"\nPlease enter elements for Matrix 1 ({rows1}x{cols1}):")
    for i in range(rows1):
        row =[]
        print(f"Row {i+1}:")
        for j in range(cols1):
            element = int(input(f"  Element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix1.append(row)

    matrix2= []
    print(f"\nPlease enter elements for Matrix 2 ({rows2}x{cols2}):")
    for i in range(rows2):
        row= []
        print(f"Row {i+1}:")
        for j in range(cols2):
            element = int(input(f"  Element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix2.append(row)

    print("\nMatrix 1 you entered is:")
    print(matrix1)
    print()
    print("Matrix 2 you entered is:")
    print(matrix2)

    print('\nThe required resultant matrix is:-', multiply_matrices(matrix1, matrix2))
