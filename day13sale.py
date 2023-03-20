# Ask for price of item
# Subtract by 10
# Return formatted string

def intput(prompt):
    res = int(input(prompt))
    return res

orig_price = intput('Enter the original price: \n')
new_price = orig_price - 10
print(f'The new price is ${new_price}')