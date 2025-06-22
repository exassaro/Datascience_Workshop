class Bank:
    def __init__(self,accountholder,balance):
        self.name=accountholder
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient fund")
        self.balance-=amount
        return self.balance
        
    def checkbalance(self):
        return self.balance
        
if __name__=="__main__":
    person = Bank("shahin",5000)
    
    print(person.checkbalance())
    
    print(person.deposit(1000))
    
    print(person.withdraw(10000))
    
    print(person.checkbalance())