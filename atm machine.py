correct_username = "pavan"
correct_password = "12345"
correct_pin = "4321"

balance = 10000
transactions = 0

login_attempts = 0

while login_attempts < 3:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    if username == correct_username and password == correct_password:
        print("Login Successful ")
        break
    else:
        print("Invalid Credentials ")
        login_attempts += 1

if login_attempts == 3:
    print("Account Blocked ")
else:

    pin_attempts = 0
    
    while pin_attempts < 3:
        pin = input("Enter 4-digit PIN: ")
        
        if pin == correct_pin:
            print("PIN Verified ")
            break
        else:
            print("Wrong PIN ")
            pin_attempts += 1
    
    if pin_attempts == 3:
        print("Account Blocked ")
    
    else:
        
        while True:
            print("\natm menu")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                print("Current Balance:", balance)
                transactions += 1
            
            elif choice == "2":
                amount = int(input("Enter amount to deposit: "))
                balance += amount
                print("Amount Deposited Successfully ")
                transactions += 1
            
            elif choice == "3":
                amount = int(input("Enter amount to withdraw: "))
                
                if amount <= balance:
                    balance -= amount
                    print("Withdraw Successful ")
                else:
                    print("Insufficient Balance ")
                transactions += 1
            
            elif choice == "4":
                print("Thank You for Using ATM ")
                break
            
            else:
                print("Invalid Option ")
        
        print("Total Transactions:", transactions)