import mysql.connector

class Customer:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="",        # db host
            user="",        # db username
            password="",    # db password
            database=""     # db name
        )
        self.cursor = self.cnx.cursor()


    # displaying details of the account for given account number

    def displayDetails(self, acc_num):
        sql = """SELECT * FROM Account WHERE account_number = %s"""
        val = (acc_num,)
        self.cursor.execute(sql, val)
        account_details = self.cursor.fetchone()        # record from database is being assigned to account_details
        name = account_details[1]
        surname = account_details[2]
        age = account_details[3]
        phone_number = account_details[4]
        account_balance = account_details[5]
        account_number = account_details[6]
        print(f"Account holder's details:\n\nName: {name} {surname}, age {age}\nPhone number: {phone_number}\nAccount balance: {account_balance}\nAccount number: {account_number}")
        go_on = str(input("\n\nClick any key to proceed "))
        if go_on == '':
            pass

    
    def withdrawMoney(self, acc_num):
        sql = """SELECT account_balance FROM Account WHERE account_number = %s"""
        val = (acc_num,)
        self.cursor.execute(sql, val)
        account_balance = self.cursor.fetchone()[0]     # account balance from the database is being assigned to account_balance
        while True:
            amountToWithdraw = float(input("Please enter the amount to withdraw: "))

            # if user gives too much of a amount to be withdrawn, he is prompted to enter smaller number, the iteration starts again
            # if amount to be withdrawn is smaller or equal to available funds, the loop breaks out to go on

            if amountToWithdraw > account_balance:  
                print("Insufficient funds, please enter smaller amount")
                continue
            break


        updated_account_balance = account_balance - amountToWithdraw
        updated_sql = """UPDATE Account SET account_balance = %s WHERE account_number = %s"""
        updated_val = (updated_account_balance, acc_num)
        self.cursor.execute(updated_sql, updated_val)
        self.cnx.commit()
        print(f"{amountToWithdraw} withdrawn! Your account balance is currently {updated_account_balance}")


    def depositMoney(self, acc_num):
        while True:
            amountToDeposit = float(input("Please enter the amount you wish to deposit: "))
            if amountToDeposit < 0:
                print("Amount can't be negative. Please try again")
                continue
            break
        sql = """SELECT account_balance FROM Account WHERE account_number = %s"""
        val = (acc_num,)
        self.cursor.execute(sql, val)
        account_balance = self.cursor.fetchone()[0]
        updated_account_balance = account_balance + amountToDeposit
        updated_sql = """UPDATE Account SET account_balance = %s WHERE account_number = %s"""
        updated_val = (updated_account_balance, acc_num)
        self.cursor.execute(updated_sql, updated_val)
        self.cnx.commit()
        print(f"{amountToDeposit} deposited! Your account balance is currently {updated_account_balance}")


    def transferMoney(self, acc_num):
        sql = """SELECT account_balance FROM Account WHERE account_number = %s"""
        val = (acc_num,)
        self.cursor.execute(sql, val)
        sender_account_balance = self.cursor.fetchone()[0]

        while True:
            amount_to_be_transferred = float(input("How much would you like to transfer? "))

            # if user wants to transfer the amount bigger than available, he is prompted to enter smaller amount

            if amount_to_be_transferred > sender_account_balance:
                print("Insufficient funds, please enter smaller amount")
                continue

            # if the amount is smaller or equal to available funds, it leaves the loop

            while True:
                # searching for receiver account by entering his/her account number
                # SELECT EXISTS returns a tuple with 1 (True) if record exists in the database and 0 if it does not (False)
                receiver_account_number = int(input("Please enter the account number you wish to transfer money to: "))
                receiver_exists_sql = """SELECT EXISTS(SELECT * FROM Account WHERE account_number = %s)"""
                self.cursor.execute(receiver_exists_sql, (receiver_account_number,))
                account_exists = self.cursor.fetchone()
                if account_exists[0]:   # if it exists
                    # it takes receiver's account balance and updates it based on the enter amount by the sender
                    receiver_sql = """SELECT account_balance FROM Account WHERE account_number = %s"""
                    self.cursor.execute(receiver_sql, (receiver_account_number,))
                    receiver_account_balance = self.cursor.fetchone()[0]
                    updated_receiver_account_balance = receiver_account_balance + amount_to_be_transferred
                    updated_receiver_balance_sql = """UPDATE Account SET account_balance = %s WHERE account_number = %s"""
                    updated_receiver_balance_val = (updated_receiver_account_balance, receiver_account_number)
                    self.cursor.execute(updated_receiver_balance_sql, updated_receiver_balance_val)

                    # then sender's account balance is being updated
                    updated_sender_account_balance = sender_account_balance - amount_to_be_transferred
                    updated_sender_balance_sql = """UPDATE Account SET account_balance = %s WHERE account_number = %s"""
                    updated_sender_balance_val = (updated_sender_account_balance, acc_num)
                    self.cursor.execute(updated_sender_balance_sql, updated_sender_balance_val)
                    self.cnx.commit()
                    print(f"{amount_to_be_transferred} transferred to {receiver_account_number}. Current balance: {updated_sender_account_balance}")
                    return
                else:
                    print("Sorry, the account with that number does not exist. Please try again.")
                    continue


    def deleteAccount(self, acc_num):
        while True:
            confirm = str(input(f"Are you sure you want to delete the account with number {acc_num}? Y/N: "))
            if confirm == "Y":
                sql = """DELETE FROM Account WHERE account_number = %s"""
                val = (acc_num,)
                self.cursor.execute(sql, val)
                print(f"Account {acc_num} has been deleted!")
                self.cnx.commit()
                return
            elif confirm == "N":
                return
            else:
                print("Please enter Y or N: ")
                continue

    def closeConnection(self):
        self.cnx.close()