def my_generator():
    for x in range(1,5):
        yield x*10

def my_function():
        my_list=[]
        for x in range(1,5):
            my_list.append(x*10)
        return my_list
    

print(my_function())
print(my_generator())

g= my_generator()
print(next(g))
print(next(g))

