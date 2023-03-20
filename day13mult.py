# Ask for name and two whole numbers
# Process the multiplication
# Return result in formatted string

def intput(prompt):
    res = int(input(prompt))
    return res

print('##### Multiplication ##### \n')
name = input('What is your name? \n').capitalize()
print(f'Hello {name}! Today we are going to have fun with numbers. \n')
num1 = intput('Enter the first number: ')
num2 = intput('Enter the second number: ')

num3 = num1 * num2

print(f'The product is {num3}')