# Q23 Write a program to Count set bits in a number.

def count_set_bits(n):
    count = 0

    while n >0:
        count += n % 2
        n = n// 2
    return count

num = int(input("Enter the number whose set bits you wanna count: "))
print("Set bits count of given number:", count_set_bits(num))