# Write a program Write function for palindrome
def is_palindrome(a):
    a=a.lower()
    i, j = 0, len(a) - 1  
    
    while i < j:
        if a[i] != a[j]:  
            return False
            
        i += 1
        j -= 1
    return True


a= input('Enter the word or number for which you wanna check if it is palindrome or not:- ')
if is_palindrome(a):
    print("Yes, it's a palindrome  ")
else:
    print("No, it's not a palindrome  ") 