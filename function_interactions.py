from random import shuffle

#initial list
sticks=['-','--','---','----']

#mixing sticks
def mix(my_list):
    shuffle(my_list)
    return(my_list)


#choos number 
def try_your_luck():
    a_try=''
    while a_try not in ['1','2','3','4']:
        a_try=input("choose a number: ")
        
    return int(a_try)

#check players try
def verify_try(a_list,a_try):
    if a_list[a_try-1]== '-':
        print("whash the dishes")
    else:
        print("This time ypu are safe")
    print(f"This is what you got {a_list [a_try- 1]}")

mixed_sticks = mix(sticks)
selection = try_your_luck()
verify_try(mixed_sticks,selection)

          


