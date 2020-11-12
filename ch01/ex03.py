'''Exercise 3: Write a program to prompt the user for hours and rate per hour to
compute gross pay.'''
# Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours
hour=int(input("enter your hours!: "))
rate=float(input("enter your rate!: "))
if hour > 40:
	pay=(hour - 40)*rate*2 +40 *rate
else:
	pay=hour*rate
print('your pay is: ',pay)