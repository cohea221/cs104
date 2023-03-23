import math
from helpers import *


num_base = input_validate_int('Enter the base number: \n')
num_exp = input_validate_int('Enter the number to raise to: \n')

num_result = math.pow(num_base, num_exp)

print(f'The number {num_base} raised to the {num_exp} power is {int(num_result)}')