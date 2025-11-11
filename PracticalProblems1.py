def return_distincs(num1,num2,num3):
    max_num= max(num1,num2,num3)
    min_num= min(num1,num2,num3)
    middle= sorted([num1,num2,num3])[1]
    
    total=sum([num1,num2,num3])
    
    if total>15:
        return max_num
    elif total<10:
        return min_num
    else:
        return middle
    
print(return_distincs(1,4,5))
        