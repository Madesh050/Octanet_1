class ATM:
    def __init__(self):
        self.balance = 500000
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"DEPOSITED AMOUNT: Rs{amount:.2f}")
            print(f"DEPOSITED AMOUNT: Rs{amount:.2f}")
            print("\nAVAILABLE BALANCE:",self.balance)
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"WITHDRAWN AMOUNT: Rs{amount:.2f}") 
                print(f"WITHDRAWN AMOUNT: Rs{amount:.2f}")
                print("\nAVAILABLE BALANCE:",self.balance)
            else:
                print("\t***********INSUFFICIENT FUNDS***********")

    def check_balance(self):
        self.transaction_history.append(f"AVAILABLE BALANCE: Rs{self.balance:.2f}")
        print(f"AVAILABLE BALANCE: Rs{self.balance:.2f}")

    def print_transaction_history(self):
        if self.transaction_history:
            print("TRANSACTION HISTORY:")
            self.transaction_history.append(f"CURRENT BALANCE: Rs{self.balance:.2f}")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("NO TRANSACTION YET")

def main():
    atm = ATM()
    print("WELCOME TO X BANK\n\nINSERT YOUR CARD")
    password=5050 
    choice=0
    pin=int(input("\nENTER THE FOUR DIGIT SECRET PIN:\n\n"))
    if pin==password:
        while choice!=6:
            print("\n******MENU******")
            print("1. CHECK BALANCE")
            print("2. WITHDRAW")
            print("3. CASH DEPOSIT")
            print("4. TRANSACTION HISTORY")
            print("5. PIN CHANGE")
            print("6. CANCEL")
            choice = input("Choose an option (1-6): ")
            if choice == '3':
                amount = float(input("ENTER THE AMOUNT TO DEPOSIT: "))
                atm.deposit(amount)
            elif choice == '2':
                amount = float(input("ENTER THE AMOUNT TO WITHDRAW: "))
                atm.withdraw(amount)
            elif choice == '1':
                atm.check_balance()
            elif choice == '4':
                atm.print_transaction_history()
            elif choice == '5':
                newpin=int(input("ENTER THE NEW PIN:"))
                password=newpin
                print("\nPIN SET SUCCESSFULLY")
                pin=int(input("\nENTER THE PIN:\n\n"))
                if pin!=newpin:
                    print("\t*********INCORRECT PIN**********")
                    break
            elif choice == '6':
                print("\t***********SESSION ENDED***********")
                break
            else:
                print("Invalid option. Please choose again.")
    else:
        print("\n\n***********INCORRECT PIN*************")
if __name__ == "__main__":
    main()
