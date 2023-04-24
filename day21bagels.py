amt_of_bagel = int(input('How many bagels do you want? '))

if amt_of_bagel < 6:
    print(f'Price is ${amt_of_bagel * .75:.2f}')
else:
    print(f'Price is ${amt_of_bagel * .6:.2f}')