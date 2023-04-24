income = int(input('Enter your income: '))

if income <= 20000:
    print(f'Your tax is ${income * .2:.2f}')
elif income <= 50000:
    out = ((income - 20000) * .25) + 4000
    print(f'Your tax is ${out:.2f}')
else:
    out = ((income - 50000) * .35) + 11500
    print(f'Your tax is ${out:.2f}')
    