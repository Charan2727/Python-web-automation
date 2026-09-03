'''
1. Using string format we can create a new string
'''
sname = input("Please enter surname  :")
fname = input("Please enter first name :")
lname = input("Please enter last name  :")


# one way of string concatenation 
print(' \n Full anme is : ',sname, ' ', fname, ' ',lname)

# another way of string concatenation 
print(' \n Full anme is : ' + sname + ' ' + fname + ' ' + lname)

## concatenation using format string function
print('\n Full anme is : {0} {1} #{2}'.format(sname, fname, lname))
