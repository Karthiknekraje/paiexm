class BankAccountOpeningChatbot:
    def __init__(self):
        self.current_step = 0
        self.questions = [
            "Welcome to our bank! To open a new account, I need to ask you a few questions.",
            "Could you please provide your full name?",
            "What is your date of birth? (Format: DD/MM/YYYY)",
            "Could you please provide your address?",
            "Which type of account are you interested in? (e.g., Savings, Checking)",
            "How much initial deposit would you like to make?",
            "Thank you for the information. We will process your application and get back to you shortly."
        ]
        self.responses = []

    def get_response(self, user_input):
        if self.current_step < len(self.questions):
            self.responses.append(user_input)
            response = self.questions[self.current_step]
            self.current_step += 1
        else:
            response = "We have completed the account opening process. Is there anything else I can assist you with?"
        return response

    def start_chat(self):
        print("Hello! I am your bank's virtual assistant.")
        print("How can I help you today?")
        while True:
            user_input = input("You: ").lower()
            if user_input in ['quit', 'exit', 'thank you']:
                print("Chat ended.")
                break
            response = self.get_response(user_input)
            print("Bank Bot:", response)

# Example usage
if __name__ == "__main__":
    bank_bot = BankAccountOpeningChatbot()
    bank_bot.start_chat()
