# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

def computation(hour,rate):
	hour=input("enter your hours!: ")
	rate=input("enter your rate!: ")
	try:
		hour=int(hour)
		rate=float(rate)
		if hour > 40:
			pay=(hour - 40)*rate*2 +40 *rate
		else:
			pay=hour*rate
		print('your pay is: ',pay)

	except ValueError:
		print('please enter numeric input')
computation(29,10)