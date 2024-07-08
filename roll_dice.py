import random as rd


class Dice:
    def roll(self):
        first_number = rd.randint(1, 6)
        second_number = rd.randint(1, 6)
        return first_number, second_number

dice = Dice()
print(dice.roll())

