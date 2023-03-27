#Chris O'Hea CS104 Hw4


# Steps:
# Ask for total
# Print tip options 10, 15, 20
# Ask for tip
# Calculate tip
# Return formatted string

# Not really necessary but I'm slowly adding re-usable parts to an external "helpers" module
def floatput(prompt):
    res = float(input(prompt))
    return res

total = floatput('Enter total on bill: \n$')

#Line Break
print('\n')

tip1 = total * .1
tip2 = total * .15
tip3 = total * .2
print(f'Tip Options: \n10% tip: ${tip1:.2f} \n15% tip: ${tip2:.2f} \n20% tip: ${tip3 :.2f}')

#Line Break
print('\n')

tip = floatput('Enter tip (without %): \n')

#Line Break
print('\n')

# Getting tip -> percent
tip_rate = tip / 100
tip_calc = total * tip_rate

print(f'Bill total is: ${total:.2f} \nTip percent is {tip:.2f}% \nTip is ${tip_calc:.2f} \nTotal after tip is ${tip_calc + total:.2f}')