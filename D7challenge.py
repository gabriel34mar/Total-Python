class Person:
    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name


class Customer(Person):
    def __init__(self, name, last_name,account_number,balance):
        super().__init__(name, last_name)
        self.account_number=account_number
        self.balance=float(balance)

    def __str__ (self):
        return f"Hi {self.name} {self.last_name}, your account balance is {self.balance}"

    def deposit(self):
        # Pido la cantidad, la convierto a float y la valido
        try:
            amount_str = input("How much would you like to add? ")
            amount = float(amount_str)
            if amount <= 0:
                print("Please enter an amount greater than 0.")
                return self.balance
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return self.balance

        # Actualizo el balance del objeto y lo devuelvo
        self.balance += amount
        return self.balance
    
    def withdraw(self):
        # Pido la cantidad, la convierto a float y la valido
        try:
            amount_str = input("How much would you like to withdraw? ")
            amount = float(amount_str)
            if amount <= 0:
                print("Please enter an amount greater than 0.")
                return self.balance
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return self.balance

        # Verifico fondos suficientes
        if amount > self.balance:
            print("Insufficient funds.")
            return self.balance

        # Resto del balance y devuelvo el nuevo balance
        self.balance -= amount
        return self.balance

customer1 = Customer("Ana", "Lopez", "12345", 1000)
print(customer1)
customer1.deposit()
print(customer1)
customer1.withdraw()
print(customer1)

