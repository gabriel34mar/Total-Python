coffe_prices=[('cappuccino',1.5),('espreso',1.2),('mocha',1.9)]

for coffee,price in coffe_prices:
    print(coffee)

def most_expensive(list_of_prices):
    highest_price=0
    my_most_expensive_cofee= ''
    
    for coffee,price in list_of_prices:
        if price>highest_price:
            highest_price=price
            my_most_expensive_cofee=coffee
        else:
            pass
    return (my_most_expensive_cofee,highest_price)

coffee, price= most_expensive(coffe_prices)

print(f"The most expensive coffe is {coffee}, whose price is {price}")

    