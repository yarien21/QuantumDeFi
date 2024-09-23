import sys
import os
from datetime import datetime, timedelta
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'MintBot')))  # Add MintBot to sys path

from mint_bot import MintBot  # Import MintBot correctly
from vault_bot import VaultBot

# Dictionary or DB to store user information and subscription data
user_data = {}

class BotPricing:
    def __init__(self):
        self.vaultbot_price_30_days = 30  # $30 for 30 days VaultBot
        self.vaultbot_price_90_days = 75  # $75 for 90 days VaultBot
        self.vaultbot_price_180_days = 150  # $150 for 180 days VaultBot
        self.vaultbot_price_360_days = 280  # $280 for 360 days VaultBot
        self.current_promo = True  # Promo status for MintBot inclusive offer

    #   def display_vaultbot_options(self):
    def display_pricing_info(self):
        if self.current_promo:
            print("Promo: MintBot is currently FREE for a limited time with 90days, 180days, and 360days VaultBot subscriptions!")
        print(f"VaultBot Subscription: ${self.vaultbot_price_30_days} for 30 days.")
        print(f"VaultBot Subscription: ${self.vaultbot_price_90_days} for 90 days (MintBot is included with VaultBot subscription for free till promo last).")
        print("MintBot is not available as a 30-day standalone subscription.")
        print("Standalone MintBot options: 4 days for $5, 7 days for $10, or 21 days for $30.")
        print("Save by subscribing to VaultBot now!")

    #   def display_mintbot_options(self):
    def display_mintbot_extension_options(self):
        print("MintBot Extension Options:")
        print("1. 4 days for $5")
        print("2. 7 days for $10")
        print("3. 21 days for $30 (8% discount if subscribed early bird discount!)")


    def display_vaultbot_options(self):

    def calculate_savings(self):
        # Calculate cost savings by choosing VaultBot over MintBot after promo
        return self.mintbot_future_price - self.vaultbot_price_30_days

    def savings_for_vaultbot_bundle(self, plan_duration):
        # Plan duration is in days (30, 90, 180, 360 days)
        months = plan_duration / 30
        
        # During promo, MintBot is free, so the user saves the MintBot price for the duration of the plan
        if self.current_promo:
            total_savings = months * self.mintbot_future_price
            return total_savings
        else:
            return 0  # No savings if promo is not active

    def display_pricing_info(self):
        if self.current_promo:
            print("Promo: MintBot is currently FREE for a limited time with 90days, 180days, and 360days subscriptions!")
        print(f"VaultBot Subscription: ${self.vaultbot_price_30_days} for 30 days.")
        print(f"VaultBot Subscription: ${self.vaultbot_price_90_days} for 90 days (discounted rate).")
        print(f"MintBot will cost ${self.mintbot_future_price} per month after the promo ends.")
        print(f"Save ${self.calculate_savings()} per month by subscribing to VaultBot now!")

    def display_vaultbot_90_day_savings(self):
        # Calculate the total savings over the entire 90 days
        total_price_for_30_days_plan = self.vaultbot_price_30_days * 3  # For 90 days, you'd pay for 3 x 30 days
        total_savings = total_price_for_30_days_plan - self.vaultbot_price_90_days  # The difference between 30-day and 90-day plan

        print(f"By subscribing to VaultBot for 90 days, you save ${total_savings:.2f} compared to paying for 30 days three times!")


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
    user = user_data.get(user_id)
    
    if user:
        signup_time = user['signup_time']
        current_time = datetime.now()
        
        # Check if 35.5 hours have passed
        time_diff = current_time - signup_time
        if time_diff >= timedelta(hours=35.5):
            print(f"35.5 hours have passed for user {user_id}. Triggering final subscription decision.")
            final_decision_prompt(user_id)

# Final prompt at 35.5 hours with three choices
def final_decision_prompt(user_id):
    print(f"User {user_id}, please make your final choice:")
    print("1. Extend MintBot: 4 days for $5")
    print("2. Extend MintBot: 7 days for $10")
    print("3. Extend MintBot: 21 days for $30 (No more 8% early bird discount)")
    print("4. Upgrade to VaultBot: 30 days for $30, 90 days for $75 (with free MintBot), 180 days for $150, 360 days for $280")
    print("5. Exit MintBot at 36 hours if no choice is made.")

# Cutoff access at 36 hours if no decision is made
def cutoff_after_36_hours(user_id):
    user = user_data.get(user_id)
    
    if user:
        signup_time = user['signup_time']
        current_time = datetime.now()
        
        # Check if 36 hours have passed
        if current_time - signup_time >= timedelta(hours=36):
            if user['subscription_status'] == 'free_trial':
                print(f"User {user_id}'s free trial has ended. Cutting off access to MintBot.")
                user['subscription_status'] = 'cutoff'
            else:
                print(f"User {user_id} is already a paid subscriber or has exited.")

# Main function with pricing and bot selection
def main():
    pricing = BotPricing()
    
    print("Select Bot:")
    print("1. MintBot (Simulated Trading)")
    print("2. VaultBot (Live Trading)")
    pricing.display_pricing_info()  # Display the pricing info, promo, and savings

    choice = input("Enter choice (1 or 2): ")
    print(f"Choice entered: {choice}")

    user_id = "user_123"  # Simulating a user ID for the demonstration
    
    # Simulate user signing up for a free trial
    if choice == '1':
        sign_up_user(user_id, "Yusmida Arien", "smidaarien@gmail.com")
        print("MintBot is FREE during the promo!")
        bot = MintBot()  # Use MintBot for simulation
        bot.run_simulation()  # Run simulation
        
        # Simulate time passing to 35.5 hours (for testing, this can be shortened)
        time.sleep(5)  # Simulate passage of time
        check_time_and_trigger_final(user_id)
        
    elif choice == '2':
        print("Choose VaultBot subscription plan:")
        print("1. 30 days for $30")
        print("2. 90 days for $75 (with free MintBot during promo)")
        print("3. 180 days for $150")
        print("4. 360 days for $280")

        vault_choice = input("Enter VaultBot subscription plan (1-4): ")

        if vault_choice == '2':  # 90-day plan
            pricing.display_vaultbot_90_day_savings()  # Show 90-day vs 30-day savings
            bot = VaultBot(initial_balance=50000)  # Use VaultBot for live trading
            bot.execute_trade()

        elif vault_choice == '1':
            bot = VaultBot(initial_balance=50000)  # Use VaultBot for live trading
            bot.execute_trade()

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
