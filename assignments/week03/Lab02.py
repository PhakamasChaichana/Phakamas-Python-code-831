
balance = 1000
pin ="1234"
entered_pin = input("Enter PIN: ")
if entered_pin == pin: 
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
if choice == "4":
    break

if choice == "3":
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("{amount}deposited.New balance is {balance}Baht.")
if choice == "2":
    amount = float(input("Enter amount towithdraw: "))
if choice == "1":
    print("Your balance is:{balance}Baht")
else: 
    print("Invalid option.Please try again.")