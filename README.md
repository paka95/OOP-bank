# OOP-bank
bank system using OOP principles (with MySQL)

System allows for creating a new account and then interacting with it. The available options include:
- displaying account's details
- withdrawing funds
- depositing funds
- transferring funds
- deleting an existing account

There is a basic value and input validation. User is prompted to reenter new value if it is wrong or not found in the database.

## How to use
```
Clone the repository
Then edit the lines in customer.py and account.py files, so that it can connect with your database (use your database data)
Install MySQL connector using "pip install mysql-connector-python" command (mysql-connector-python==8.0.31 used in this project)
Start the program with "python main.py" command
```

## Snippets of the program in use:
1. Start of the program: \
![start](https://user-images.githubusercontent.com/94203043/209845187-7e861417-f171-4a6a-818c-1c7084b92412.png)


2. Validation when specifying options: \
![mainmenuoptionvali](https://user-images.githubusercontent.com/94203043/209845267-85d96168-b4b1-4596-ac87-e46b7cc8d8c1.png)
![mainmenuoptionvali2](https://user-images.githubusercontent.com/94203043/209845276-0a44cdc1-5463-4438-9fb8-eb0cfaa99e92.png)


3. Creating account: \
![creating account](https://user-images.githubusercontent.com/94203043/209845104-b5015c87-2c35-4b00-9161-3fe67a8b616b.png)


4. Logging into account after creation: \
![logingintoaccwithvali](https://user-images.githubusercontent.com/94203043/209845830-9f5d29da-d297-4da0-a8e1-dbd5b997eaa3.png)


5. Account number and PIN validation when logging in \
![failedvalidationaccnum](https://user-images.githubusercontent.com/94203043/209846212-326ef4d1-aa87-4a46-add7-7d2af1f2a273.png)
![pinvalidationfailed](https://user-images.githubusercontent.com/94203043/209846210-5ccf4cb2-7581-4c58-b055-a9605179b47c.png)


6. Displaying account details: \
![accdets](https://user-images.githubusercontent.com/94203043/209846341-caedb9a1-fac9-4f20-8b23-da067d325ba5.png)


7. Depositing and withdrawing money (with validation)
![depositwithdrawvalidationn](https://user-images.githubusercontent.com/94203043/209846427-5d4a72e0-3878-4819-91d9-631717d5004f.png)


8. Transferring money to other user (with validation)
![transferringwithvalidation](https://user-images.githubusercontent.com/94203043/209846479-0497cb41-db19-4637-92d4-46342c6119b1.png)


9. Returning to main menu (logging out) \
![goingbacktomenu logginout](https://user-images.githubusercontent.com/94203043/209846680-5f889cbf-3853-43f1-83e4-ceb16f86789f.png)


10. Database view \
![dbss](https://user-images.githubusercontent.com/94203043/209846725-4d99aad7-19ba-47cc-b074-a2b15741400e.png)


11. Deleting account \
![deletingacc](https://user-images.githubusercontent.com/94203043/209846759-6f31434f-c4bb-4d97-a42c-f9f9b3283001.png)


12. Database after deletion \
![dbafterdelete](https://user-images.githubusercontent.com/94203043/209846781-8266d0a5-ae2a-4eda-ac85-df4e811171e9.png)


## Issues to amend
System does have some small bugs that could be fixed in the future, for example:
- trial counter in account number validation does not take into consideration values of wrong type (if you type numerical values two times and then two alphanumerical values it does not stop after 3 attempt).
- PIN is displayed to the user after creation (in reality such private data is sent secretly to the user using some other form, but here it is different due to simplicity, program just simulates the work of a real bank)
- PIN is not hashed in DB (it should be hashed, but for simplicity it is not, it is just showcasing OOP understanding)
- due to the Main Menu structure, if user enters PIN wrong 3 times, it is exiting the whole program and not just returning to Main Menu
