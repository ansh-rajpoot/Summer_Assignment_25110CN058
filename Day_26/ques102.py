# Write a program to Create voting eligibility
# system.
def check_voting_eligibility(age):
    if age >= 18:
        return True
    else:
        return False

user_age =int(input("Enter your age: "))

 

if check_voting_eligibility(user_age):
    print("\nYou are eligible to vote!")
else:
    years_left = 18 - user_age
    print(f"\nYou are not eligible to vote yet. You need to wait {years_left} more year(s).")
