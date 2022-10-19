
#question 1 
class power:
  def _init_(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z
  def sqnum (self):
    a=self.x*2+self.y2+self.z*2
    print("The square of sum of number is",a)
d=power(3,4,5)
d.sqnum()


#question 2
class calculator:
    def _init_(jayesh,x,y):
        jayesh.x=x
        jayesh.y=y
        print(jayesh.x)
        print(jayesh.y)
    def add(jayesh):
        print("The addition is",jayesh.x+jayesh.y)
    def sub(jayesh):
        print("the substraction is",jayesh.x-jayesh.y)
    def mul(jayesh):
        print("The multiplication is",jayesh.x*jayesh.y)
    def div(jayesh):
        print("the division is",jayesh.x/jayesh.y)
z=calculator(10,30) 
z.add()
z.sub()
z.mul()
z.div()



#question 3 
word = input("Input a word to reverse: ")
 
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


#question 4
class Account:
  def _init_(self,title=None,balance=0):
    self.title=title
    self.balance=balance
class SavingsAccount(Account):
  def _init_(self,title=None,balance=0,interestRate=0):
  
    super()._init_(title,balance)
    self.interestRate=interestRate

acc = Account("ashish",5000)
print(acc.title)
print(acc.balance)

saving_acc = SavingsAccount("Ashish",5000,5)
print(saving_acc.interestRate)



#question 5
class Account:
    def _init_(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def deposit(self, amount):
        
        self.balance += amount
        print("\n Amount Deposited:",amount)

    def getBalance(self):
        print("\n Net Available Balance=",self.balance)

class SavingsAccount(Account):
    def _init_(self, title=None, balance=0, interestRate=0):
            super()._init_(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        
        interestAmount=(self.interestRate*self.balance)/100
        print("Interest amount is: ",interestAmount)



demo1 = SavingsAccount("jayesh", 2000, 5) 
demo1.deposit(500)
demo1.withdrawal(2000)
demo1.getBalance()
demo1.interestAmount()


