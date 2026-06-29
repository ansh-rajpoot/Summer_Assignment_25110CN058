def row_wise_sum(matrix):
    result = []
    for row in matrix:
        total = 0
        for element in row:
            total +=element
        result.append(total)
    return result

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix1= []
print(f"\nPlease enter elements for Matrix ({rows}x{cols}):")
for i in range(rows):
    row =[]
    print(f"Row {i+1}:")
    for j in range(cols):
        element = int(input(f"  Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)

print("\nThe Matrix   entered is:")
print(matrix1)

print('\nThe required row wise sum is:-', row_wise_sum(matrix1))
