def test(number1,number2,*args,**kwargs):
    print(f"The firs number is {number1}")
    print(f"The second number is {number2}")
    for arg in args:
        print(f"arg = {arg}")
        
        
    for key,value in kwargs.items():
        print(f"{key} = {value}")
        
   
args=[120,1030,130,130]
kwargs = {'x':'one','y':'five','z':'two'}

test(15,50,120,1030,130,130,x='one',y='five',z='two')
test(15,50,*args,**kwargs)

