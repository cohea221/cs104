num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))
           
nums = [num1, num2, num3]
sorted_nums = sorted(nums)
           
average = (sorted_nums[1] + sorted_nums[2]) / 2
           
print(f'The average of the two highest is {average}')