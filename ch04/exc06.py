# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

def computation(hour,rate):
	hour=input("enter your hours!: ")
	rate=input("enter your rate!: ")
	try:
		hour=int(hour)
		rate=float(rate)
		if hour > 40:
			pay=(hour - 40)*rate*1.5 +40 *rate
		else:
			pay=hour*rate
		print('your pay is: ',pay)

	except ValueError:
		print('please enter numeric input')
computation(0,0)

# another way 

def comput(hour,rate):
	if hour > 40:
		pay=(hour - 40)*rate*1.5 +40 *rate
	else:
		pay=hour*rate
	return pay
hour=int(input("enter your hours!: "))
rate=float(input("enter your rate!: "))
Pay=comput(hour,rate)
print('pay: ',Pay)


