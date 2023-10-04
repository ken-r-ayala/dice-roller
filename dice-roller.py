# Dice Roller Application is used for fun only

import random

dice_type = input("What kind of Dice? D6, D8, D4, etc.: ")
dice_quantity = input("How many would you like to roll?: ")
dice_number_chosen = int(dice_quantity) + 1

if dice_type == "D4":
    for i in range(1, dice_number_chosen):
        print(random.randint(1, 4))
        dice_number_chosen = int(dice_number_chosen) - 1
        if dice_number_chosen == 0:
            break
        else:
            continue
elif dice_type == "D6":
    for i in range(1, dice_number_chosen):
        print(random.randint(1, 6))
        dice_number_chosen = int(dice_number_chosen) - 1
        if dice_number_chosen == 0:
            break
        else:
            continue
elif dice_type == "D8":
    for i in range(1, dice_number_chosen):
        print(random.randint(1, 8))
        dice_number_chosen = int(dice_number_chosen) - 1
        if dice_number_chosen == 0:
            break
        else:
            continue
elif dice_type == "D10":
    for i in range(1, dice_number_chosen):
        print(random.randint(1, 10))
        dice_number_chosen = int(dice_number_chosen) - 1
        if dice_number_chosen == 0:
            break
        else:
            continue
elif dice_type == "D12":
    for i in range(1, dice_number_chosen):
        print(random.randint(1, 12))
        dice_number_chosen = int(dice_number_chosen) - 1
        if dice_number_chosen == 0:
            break
        else:
            continue
elif dice_type == "D20":
    for i in range(1, dice_number_chosen):
        print(random.randint(1, 20))
        dice_number_chosen = int(dice_number_chosen) - 1
        if dice_number_chosen == 0:
            break
        else:
            continue
else:
    print("Sorry, I can not understand what you are asking.")
