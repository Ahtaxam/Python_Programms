# This programm is a little bit metro ticket system 



class Metro:
    def __init__(self):
        self.balance = 0
        self.fair_price = 30
        self.no_of_ticket = 0


    def CheckBalance(self):
        return self.balance

    def DepositMoney(self,amount):
        self.balance += amount

    def PurchaseTicket(self , no):
        total = no * self.fair_price

        if self.balance >= total:
            self.balance -= total
            self.no_of_ticket += no
            return True
        else:
            return False


    
ticket = Metro()

print()
print("<----------------------Welcome to Metro Tickting System--------------------->")
print()
print()
print('<----------------------------------TODO--------------------------------------->')
print()

print("1 --------  Check Balance")
print("2 --------  Deposit Money")
print("3 --------  Purchase Tokken")
print("4 --------  Check No Of Tickets That Are Buy")
print()
q = 'y'
flag = True

while q == 'y':
    print('Press Any Key: ',end='')
    key = int(input())

    if key == 1:
        print('Your Balance is: ' , ticket.CheckBalance())
        print()

    elif key == 2:

        print('Enter amount you want to deposit: ',end='')
        amount = int(input())
        ticket.DepositMoney(amount)
        print()

    elif key == 3:
        
        print("How many Tickets You want to Buy: " ,end='')
        no = int(input())

        flag = ticket.PurchaseTicket(no)
        if flag == True:
            print("You Bought Ticket")
            print()
        else:
            print('Insufficient Balance')
            print()

    elif key == 4:
        print('You Bought Total Tickets: ' , ticket.no_of_ticket)
        print()

        print('Do you want to continue programm (yes ----- y )  ')
        q = input()
        if q == 'y':
            continue
        else:
            print("OK !! Best Of Luck")
            break
