"""Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive)."""

def absolute_sum(*nums_a):
    total=0
    for num in nums_a:
        absolute = abs(num)
        total+=absolute
    
    return total

print(absolute_sum(1, -2, 3, -4))

     