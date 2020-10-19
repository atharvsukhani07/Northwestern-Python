def quotientString(x, y):
    quotient = x//y
    remainder = x%y
    sentence = 'The quotient of {} and {} is {} with a remainder of {}.'.format(x, y, quotient, remainder)
    return sentence

def main():
    x = int(input("Enter an integer"))
    y = int(input("Enter another integer: "))
    print (quotientString(x, y))

if __name__ == '__main__':
    main()


