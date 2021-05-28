class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def getbalance(self):
        sum = 0
        for item in self.ledger:
            sum += item['amount']
        return sum
        
    def deposit(self,amount,description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def check_funds(self,amount):
        sum = self.getbalance()
        if amount > sum:
            return False
        else:
            return True

    def transfer(self,amount,destination):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": 'Transfer to ' + destination.name})
            destination.deposit(amount, 'Transfer from ' + self.name)
            return True
        else:
            return False
        

food = Category('expenses')
travel = Category('travel')
food.deposit(10,'groceries')
food.deposit(20,'food')
food.withdraw(10)
food.transfer(10,travel)
print(food.getbalance())

print(food.ledger)
print(travel.ledger)

