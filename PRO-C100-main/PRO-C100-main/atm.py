class Atm:
    def __init__(self,card_number,pin):
        self.card_number=card_number
        self.pin=pin
    def check_balance(self):
        print('your balance is 100000')
    def withdrawl(self,amount):
        new_amount=100000-amount
        print('you have withdrawl amount'+str(amount)+'.your remaining balance is '+str(new_amount))

def main():
    cardnumber=input('insert your card number')
    pin_number=input('enter your pin number')
    newuser=Atm(cardnumber,pin_number)
    print('chose your activity')
    print('1.balance enquiry  2.withdrawl')
    activity=int(input('enter activity number'))

    if(activity==1):
        newuser.check_balance()
    elif(activity==2):
        amount=int(input('enter the amount'))
        newuser.withdrawl(amount)
    else:
        print('enter a valid number')

if __name__=='__main__':
    main()
        