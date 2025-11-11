"""Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values."""
numbers=[1,-2,3]
def all_positives(numbers):
    for n in numbers:
        if n < 0:
            return False
    return True