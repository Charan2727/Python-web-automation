'''
1. "if", "elif", and "else" are conditional statements
2. "if" checks the first condition
3. "elif" checks the next condition only if the previous one is False
4. "else" runs when none of the above conditions are True

elif is used when you have multiple conditions to check — one after another
elif runs only if all previous if or elif conditions are False

'''

marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

