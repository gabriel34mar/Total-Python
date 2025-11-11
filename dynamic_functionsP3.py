"""Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count."""

def count_even(number):
    count=0
    for n in number:
        if n%2==0:
            count+=1

    return count        

nums = [1, 2, 3, 4, 10, 11]

result=count_even(nums)
print(result)