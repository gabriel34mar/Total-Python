"""Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it."""
numbers=[1,2,3,4,5,100,1001,-1]
def sum_less(numbers):
    num=0
    for n in numbers:
        if n in range(0,1000):
            num+=n
        else:
            pass
    
    return num