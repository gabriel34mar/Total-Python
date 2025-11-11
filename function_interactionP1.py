"""Create a function (throw_dice) that "throws" two random dice and returns its results (the function MUST RETURN TWO VALUES AS A RESULT, both of which must be between 1 and 6, randomly).

Pass the result of these two dice to a function called roll_result (meaning that this second function MUST RECEIVE TWO ARGUMENTS) and return -without printing it- a certain message according to the what the sum of these values results:

If the sum is less than or equal to 6:

"The sum of your dice is {sum_dice}. Unfortunate"

If the sum is greater than 6 and less than 10:

"The sum of your dice is {sum_dice}. You have a good chance"

If the sum is greater than or equal to 10:

"The sum of your dice is {sum_dice}. It looks like a winning roll"

Hint: use the random library's choice or randint method to choose a random value between 1 and 6."""
from random import randint

def throw_dice():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1, dice2

def roll_result(dice1, dice2):
    sum_dice = dice1 + dice2
    if sum_dice <= 6:
        return f"The sum of your dice is {sum_dice}. Unfortunate"
    elif 6 < sum_dice < 10:
        return f"The sum of your dice is {sum_dice}. You have a good chance"
    else:
        return f"The sum of your dice is {sum_dice}. It looks like a winning roll"

dice1, dice2 = throw_dice()
result = roll_result(dice1, dice2)
print(result)