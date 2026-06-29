def column_wise_sum(matrix):
    rows = len(matrix)
    cols =len(matrix[0])
    result =[]
    for j in range(cols):
        total = 0
        for i in range(rows):
            total +=matrix[i][j]
        result.append(total)
    return result

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix1= []
print(f"\nPlease enter elements for Matrix ({rows}x{cols}):")
for i in range(rows):
    row = []
    print(f"Row {i+1}:")
    for j in range(cols):
        element =int(input(f"  Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)
print()
print("The Matrix entered is:")
print(matrix1)

print('\nThe required column wise sum is:-', column_wise_sum(matrix1))
