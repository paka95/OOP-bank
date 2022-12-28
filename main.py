from account import Account
from customer import Customer


def bank():


    while True:
        print("""
        ***************************
            WELCOME TO OUR BANK
        ===========================
        1. Create a new account
        ===========================
        2. Access your account
        ===========================
        3. Exit
        """)

        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("You need to enter a number between 1-3")
            continue

        if choice == 1:
            new_acc = Account()
            print("Creating a new account")
            name = str(input("Enter name: "))
            surname = str(input("Enter surname: "))
            age = int(input("Enter age: "))
            phone_number = int(input("Enter phone number: "))

            new_acc.createAccount(name, surname, age, phone_number)


        elif choice == 2:
            trial_counter = 0
            while True:
                try:
                    acc_num = int(input("Please enter your account number: "))
                except ValueError:
                    print("Please enter numerical account number with 6 digits.")
                    continue

                account = Account()
                if account.doesExist(acc_num):          # method that checks in the database if entered account number is present
                    pin_trials = 0                      # if so, then it breaks out of the loop to go on
                    while True:
                        if account.pinMatches(acc_num): # method that checks in the database if entered pin matches account number
                            break
                        else:
                            pin_trials += 1
                            if pin_trials == 3:
                                print("The number of trials has been exceeded. Aborting program.")
                                return
                            continue                # starts new iteration if pin is wrong

                    while True:
                        print("""
                        1. Display account details
                        2. Withdraw money
                        3. Deposit money
                        4. Transfer money
                        5. Delete account
                        6. Back to Main Menu
                        """)
                        try:
                            choice = int(input("Enter choice: "))
                        except (TypeError, ValueError):
                            print("You need to enter a number between 1-6.")
                            continue

                        customer = Customer()
                        if choice == 1:
                            customer.displayDetails(acc_num)
                        elif choice == 2:
                            customer.withdrawMoney(acc_num)
                        elif choice == 3:
                            customer.depositMoney(acc_num)
                        elif choice == 4:
                            customer.transferMoney(acc_num)
                        elif choice == 5:
                            customer.deleteAccount(acc_num)
                            break
                        elif choice == 6:
                            customer.closeConnection()
                            break
                        else:
                            print("Please select options between 1-6")
                            continue
                    break
                
                else:
                    print("Account with this number does not exist. Please try again")
                    trial_counter += 1
                    if trial_counter == 3:
                        print("Trials exceeded. Returning to main menu")    # if user notoriously gives wrong account number
                        break                                               # he gets returned to main menu to start over
        
        elif choice == 3:
            print("Goodbye!")
            return
        else:
            print("Please enter number between 1-3")


if __name__ == '__main__':
    bank()