class BankingAssistant:
    def __init__(self):
        self.users = {}
    
    def create_account(self):
        print("Let's create your bank account!")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        address = input("Enter your address: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        initial_deposit = float(input("Enter your initial deposit amount: $"))

        account_number = len(self.users) + 1
        self.users[account_number] = {
            "name": name,
            "age": age,
            "address": address,
            "phone_number": phone_number,
            "email": email,
            "balance": initial_deposit
        }
        
        return f"Account created successfully! Your account number is {account_number}."
    
    def start(self):
        print("Welcome to the Banking Assistant!")
        while True:
            print("\nWhat would you like to do?")
            print("1. Open an Account")
            print("2. Exit")
            
            choice = input("Enter your choice (1-2): ")
            
            if choice == '1':
                print(self.create_account())
            elif choice == '2':
                print("Thank you for using the Banking Assistant. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    assistant = BankingAssistant()
    assistant.start()
