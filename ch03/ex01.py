# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input



hour=int(input("enter your hours!: "))
rate=input("enter your rate!: ")
try:
	rate=float(rate)
	if hour > 40:
		pay=(hour - 40)*rate*2 +40 *rate
	else:
		pay=hour*rate
	print('your pay is: ',pay)

except ValueError:
	print('please enter numeric input')
