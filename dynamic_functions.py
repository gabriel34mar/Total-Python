def check3_digits(list1):
    
    three_digits_list=[]
    
    for n in list1:
        if n in range (100,1000):
            three_digits_list.append(n)
        else:
            pass
    return three_digits_list
result= check3_digits([33,100,500])
print(result)    


