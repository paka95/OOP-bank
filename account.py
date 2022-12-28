import random
import mysql.connector

class Account:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="",        # db host
            user="",        # db username
            password="",    # db password
            database=""     # db name
            )
        self.cursor = self.cnx.cursor()
        

    def createAccount(self, name, surname, age, phone_number):
        self.cursor.execute("""
            create table if not exists Account (
            id int AUTO_INCREMENT PRIMARY KEY,
            name varchar(255) NOT NULL,
            surname varchar(255) NOT NULL,
            age int NOT NULL,
            phone_number int NOT NULL,
            account_balance float NOT NULL,
            account_number int (6),
            pin int(4) NOT NULL
            )
            """)

        account_number = random.randint(100000, 999999)     # system automatically assigns random account number
        pin = random.randint(1000, 10000)                   # and PIN, which user then must store somewhere or memorize
        account_balance = 0                                 # it is the only time and place 
                                                            # where user is being shown his account number and PIN
        sql = """INSERT INTO Account (
                                    account_number, 
                                    name, 
                                    surname, 
                                    age, 
                                    phone_number, 
                                    account_balance, 
                                    pin
                                    ) VALUES (%s, %s, %s, %s ,%s ,%s, %s)"""
        val = (account_number, name, surname, age, phone_number, account_balance, pin)
        self.cursor.execute(sql, val)
        self.cnx.commit()
        print(f"Account created! Your account number is {account_number}, your pin is {pin}. Please save and store them!")
        self.cnx.close()


    def doesExist(self, acc_num):
        # method to check if the account exists, SELECT EXISTS returns a tuple with 1 (True) if it does and 0 (False) if it does not
        sql = """SELECT EXISTS(SELECT * FROM Account WHERE account_number = %s)"""
        val = (acc_num,)
        self.cursor.execute(sql, val)
        record_exists = self.cursor.fetchone()
        if record_exists[0]:
            return True
        else:
            return False


    def pinMatches(self, acc_num):
        # method to check whether entered PIN matches entered account number, giving user an access if it does
        sql = """SELECT * FROM Account WHERE account_number = %s"""
        val = (acc_num,)
        self.cursor.execute(sql, val)
        account_details = self.cursor.fetchone()
        name = account_details[1]
        user_pin = account_details[7]
        while True:
            try:
                entered_pin = int(input("Enter pin: "))
                if user_pin == entered_pin:
                    print(f"Account accessed. Welcome {name}!")
                    return True
                else:
                    print("Wrong pin. Please try again.")
                    return False
            except ValueError:
                print("You need to enter numerical PIN with 4 digits. Please try again.")
                return False