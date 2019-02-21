# Input

setting = int(input('Enter the origin numbersystem: [2/8/10/16]'))
goal = input('Enter the goal numbersystem: [2/8/10/16]')
number = int(input('Enter your number:'), setting)

# convert to goal
if goal == '2':
    number = bin(number)
elif goal == '8':
    number = oct(number)
elif goal == '10':
    number = int(number)
elif goal == '16':
    number = hex(number)
else:
    print('You entered an unknown numbersystem as goal!')

print(number)