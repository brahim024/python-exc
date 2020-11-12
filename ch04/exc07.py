# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as a
# string.

def computegrade(score):
	while True:
		score=input('enter your score: ')
		try:
			score=float(score)
			if score < 0 or score>1.0:
				print('score out of the range')
			elif score >= 0.9:
				print('A')
			elif score >= 0.8:
				print('B')
			elif score >= 0.7:
				print('C')
			elif score >= 0.6:
				print('D')
			else:
				print('F')
		except ValueError:
			print('Bad score')
computegrade(0)