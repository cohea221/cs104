# Ask for total
# Ask for tip
# Calculate tip
# Return formatted string

def intput(prompt):
    res = int(input(prompt))
    return res

total = intput('Enter total on bill: \n')
tip = intput('Enter tip (without %): \n')

tip_rate = 1 / tip
tip_calc = total * tip_rate

print(f'Bill total is: ${total} \n Tip percent is {tip}% \n Tip is ${tip_calc:.2f} \n Total after tip is ${tip_calc + total:.2f}')