def repeat(*numbers):
    for i in range(len(numbers)-1):
       if numbers[i] == 0 and numbers[i+1] == 0:
        return True
    return False

print(repeat(5, 6, 1, 0, 0, 9, 3, 5))  # True
print(repeat(6, 0, 5, 1, 0, 3, 0, 1))  # False
