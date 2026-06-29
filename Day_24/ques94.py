# Write a program to Compress a string.
def compress_string(string_val):
    if not string_val:
        return ""
    compressed=[]
    count = 1
    n = len(string_val)
    
    for i in range(n - 1):
        if string_val[i] == string_val[i + 1]:
            count +=1
        else:
            compressed.append(string_val[i] + str(count))
            count= 1
            
    compressed.append(string_val[-1] + str(count))
    result = "".join(compressed)
    
    if len(result) < len(string_val):
        return result
    else:
        return string_val
    


user_str = input("Enter a string you wanna compress: ")

print("\nThe string you entered is:")
print(user_str)

print('\nThe required compressed string is:-', compress_string(user_str))
