import sys
import os
from datetime import datetime, timedelta
import time

# Check the path for MintBot and VaultBot
print(os.path.abspath(os.path.join(os.path.dirname(__file__), 'MintBot')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), 'VaultBot')))

# Add both MintBot and VaultBot to sys path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'MintBot')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'VaultBot')))

from MintBot.mint_bot import MintBot  # Import MintBot correctly
from VaultBot.vault_bot import VaultBot

# Dictionary or DB to store user information and subscription data
user_data = {}

class QuantumDefi:
    def __init__(self):
        # Unified QuantumDeFi subscription prices (includes MintBot, VaultBot, and PaperBot)
        self.price_30_days = 30  # $30 for 30 days
        self.price_90_days = 80  # $80 for 90 days
        self.price_180_days = 150  # $150 for 180 days
        self.price_360_days = 260  # $260 for 360 days
        self.current_promo = True  # Promo status for early bird offer
    
    def calculate_promo_price(self, price):
        """Calculate promo price based on active promotions."""
        if self.current_promo:
            print("15% Early Bird Discount Applied!")
            return price * 0.85  # Apply 15% discount
        return price
    
    def display_pricing_info(self):
        """Display the pricing for the QuantumDeFi subscription."""
        if self.current_promo:
            print("Promo: 15% discount for early bird promotion (first 3 days), 10% discount (7 days from launch)!")
        
        # Apply promo to each price
        price_30 = self.calculate_promo_price(self.price_30_days)
        price_90 = self.calculate_promo_price(self.price_90_days)
        price_180 = self.calculate_promo_price(self.price_180_days)
        price_360 = self.calculate_promo_price(self.price_360_days)
        
        print(f"QuantumDeFi Subscription: ${price_30:.2f} for 30 days.")
        print(f"QuantumDeFi Subscription: ${price_90:.2f} for 90 days.")
        print(f"QuantumDeFi Subscription: ${price_180:.2f} for 180 days.")
        print(f"QuantumDeFi Subscription: ${price_360:.2f} for 360 days.")

    def start_trial(self, user_id):
        """Start the 36-hour trial period for PaperBot."""
        print(f"Starting 36-hour free trial for user: {user_id}")
        self.run_simulation(bot_type="PaperBot")

    def run_simulation(self, bot_type="MintBot"):
        """Simulate the chosen bot (MintBot, VaultBot, or PaperBot)."""
        if bot_type == "MintBot":
            bot = MintBot()  # Simulate MintBot
            bot.run_simulation()
        elif bot_type == "VaultBot":
            bot = VaultBot()  # Simulate VaultBot
            bot.execute_trade()
        elif bot_type == "PaperBot":
            print("Simulating PaperBot (combined MintBot and VaultBot).")
            self.simulate_paper_bot()
        else:
            print("Invalid bot type selected.")

    def simulate_paper_bot(self):
        """Simulate PaperBot for both MintBot and VaultBot trading."""
        print("Simulating PaperBot (combined MintBot and VaultBot).")
        # mint_bot = MintBot()
        mint_bot = MintBot()  # MintBot for aggressive trading
        vault_bot = VaultBot()  # VaultBot for conservative trading
        
        # Simulate MintBot (aggressive trading)
        mint_bot.run_simulation()
        
        # Simulate VaultBot (conservative trading)
        vault_bot.execute_trade()

# Capture sign-up timestamp
def sign_up_user(user_id, name, email):
    signup_time = datetime.now()
    
    # Store user data in a simple dictionary (in real-world, this would be a database)
    user_data[user_id] = {
        'name': name,
        'email': email,
        'signup_time': signup_time,
        'subscription_status': 'free_trial',
    }

    print(f"User {name} signed up at {signup_time}")
    return user_data[user_id]

# Check time and trigger final decision at 35.5 hours
def check_time_and_trigger_final(user_id):
    """Check if 35.5 hours have passed and trigger final decision."""
    user = user_data.get(user_id)
    if user:
        signup_time = user['signup_time']
        current_time = datetime.now()
        
        # Check if 35.5 hours have passed
        time_diff = current_time - signup_time
        if current_time - signup_time >= timedelta(hours=35.5):
            print(f"35.5 hours have passed for user {user_id}. Triggering final subscription decision.")
            final_decision_prompt(user_id)

# Final prompt at 35.5 hours
def final_decision_prompt(user_id):
    """Prompt the user with the final subscription decision at the end of the free trial."""
    print(f"User {user_id}, your 36-hour free trial is almost over.")
    print("1. Subscribe to QuantumDeFi: $30 for 30 days")
    print("2. Subscribe to QuantumDeFi: $80 for 90 days")
    print("3. Subscribe to QuantumDeFi: $150 for 180 days")
    print("4. Subscribe to QuantumDeFi: $260 for 360 days")
    print("5. Exit the platform at 36 hours if no choice is made.")

# Cutoff access at 36 hours if no decision is made
def cutoff_after_36_hours(user_id):
    user = user_data.get(user_id)
    
    if user:
        signup_time = user['signup_time']
        current_time = datetime.now()
        
        # Check if 36 hours have passed
        if current_time - signup_time >= timedelta(hours=36):
            if user['subscription_status'] == 'free_trial':
                print(f"User {user_id}'s free trial has ended. Cutting off access.")
                user['subscription_status'] = 'cutoff'
                print("To continue using QuantumDeFi services, please subscribe.")
            else:
                print(f"User {user_id} is already a paid subscriber or has exited.")

# Main function with pricing and bot selection
def main():
    quantum_defi = QuantumDefi()
    
    print("Welcome to QuantumDeFi!")
    print("1. Start 36-hour Free Trial")
    print("2. View Subscription Plans")
    
    choice = input("Enter choice (1 or 2): ")
    print(f"Choice entered: {choice}")

    user_id = "user_123"  # Simulating a user ID for the demonstration
    
    # Handle the user's choice
    if choice == '1':
        sign_up_user(user_id, "John Aris", "johnaris@gmail.com")
        quantum_defi.start_trial(user_id)  # Start 36-hour trial for the user
        
        # Simulate time passing to 35.5 hours (for testing, this can be shortened)
        time.sleep(5)  # Simulate passage of time
        check_time_and_trigger_final(user_id)

        # Add this line to check if the user has been cut off after 36 hours
        cutoff_after_36_hours(user_id)  # Check for cutoff after 36 hours
        
    elif choice == '2':
        # Show subscription options for QuantumDeFi
        quantum_defi.display_pricing_info()
        subscription_choice = input("Select your subscription plan (1 for 30 days, 2 for 90 days, etc.): ")

        if subscription_choice == '1':
            print("You’ve subscribed to QuantumDeFi for 30 days!")
        elif subscription_choice == '2':
            print("You’ve subscribed to QuantumDeFi for 90 days!")
        elif subscription_choice == '3':
            print("You’ve subscribed to QuantumDeFi for 180 days!")
        elif subscription_choice == '4':
            print("You’ve subscribed to QuantumDeFi for 360 days!")
        elif subscription_choice == '5':
            print("Exiting platform. Thank you!")
        else:
            print("Invalid choice!")
            final_decision_prompt(user_id)

    else:
        print("Invalid choice! Please try again.")
        main()
        
if __name__ == "__main__":
    main()
   
