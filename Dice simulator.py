import random
def dice_img(n):
    match n:
        case 1: return "⚀"
        case 2: return "⚁"
        case 3: return "⚂"
        case 4: return "⚃"
        case 5: return "⚄"
        case 6: return "⚅"


dice = []
ch = 'r'
while ch == 'r':
    dice_value = random.randint(1,6)
    print(dice_value)

    print(dice_img(dice_value))
    dice.append(dice_value)
    print("Want to roll again(type r): ")
    ch = input()
print()



