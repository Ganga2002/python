class Bank:
    def _init_(self):
        self.balance=0
        print('-create an account-')
        self.name=input("enter name:")
        self.accntno=int(input("enter account number:"))
        self.typeof=input("enter type of account:")
    def deposit(self):
        amount=int(input("enter amount to deposit"))
        self.balance+=amount
        print("amount deposited ",amount)
    def withdraw(self):
        amount=int(input("enter amount to withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("amount withdrawn:",amount)
        else:
            print("insufficient amount")
    def display(self):
        print("account balance:",self.balance)
        
a=Bank()
a._init_()
while(1):
    print("\n1.deposit\n2.withdraw\n3.balance\n4.exit\n")
    ch=int(input("enter choice"))
    if ch==1:
        a.deposit()
    elif ch==2:
        a.withdraw()
    elif ch==3:
        a.display()
    else:
        print('wrong choice')
        exit()
