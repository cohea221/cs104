# Ask for name and two whole numbers
# Process the addition
# Return result in formatted string

def intput(prompt):
    res = int(input(prompt))
    return res

print('##### Addition ##### \n')
name = input('What is your name? \n').capitalize()
print(f'Hello {name}! Today we are going to have fun with numbers. \n')
num1 = intput('Enter the first number: ')
num2 = intput('Enter the second number: ')
num3 = intput('Enter the third number: ')
num4 = intput('Enter the fourth number: ')

total = num1 + num2 + num3 + num4
average = total / 4
print(f'The total is {total}')
print(f'The average is {average: .0f}')