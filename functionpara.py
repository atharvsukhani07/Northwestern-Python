def sumProblem(x, y):
	sum = x + y
	sentence = 'The sum of {} and {} is {}.'.format( x,y,sum)
	print(sentence)

	
def main():
	sumProblem( 2,3)
	sumProblem( 1234567890123, 535790269358)
	a = int(input("Enter an Integer: "))
	b = int(input("Enter another inetger: "))
	sumProblem( a,b)

	
main()
