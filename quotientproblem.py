def quotientProblem(x, y):
    quotient = x//y
    remainder = x%y
    sentence = 'The quotient of {} and {} is {} with a remainder of {}.'.format(x, y, quotient, remainder)
    print(sentence)


def main():
    quotientProblem(14, 3)
    x = int(input("Enter an integer"))
    y = int(input("Enter another integer: "))
    quotientProblem(x, y)


main()
