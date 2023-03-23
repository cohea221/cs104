import math
from helpers import *    

num1 = input_validate_int('Enter a number to get its absolute value: \n')
num2 = math.fabs(num1)
print(f'The absolute value of {num1} is {int(num2)}')