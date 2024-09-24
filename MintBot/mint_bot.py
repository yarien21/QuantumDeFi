import numpy as np  # For calculations like profit, risk management
import time
from datetime import datetime, timedelta

# Define the MintBot class under QuantumDeFi strategy
class MintBot:
    def __init__(self):
        self.start_time = time.time()
        self.free_trial_period = 36 * 3600  # 36 hours in seconds
        self.trial_active = True
        self.discount_eligible_until = None
        self.return_discount_window = timedelta(days=7)

    # Unified QuantumDeFi free trial simulation
    def run_simulation(self):
        """Simulate the MintBot during the trial period."""
        print("MintBot simulation running...")
        trade_profits = np.random.uniform(0.05, 0.1, 5)  # Simulating 5 trades with 5-10% profit range
        for i, profit in enumerate(trade_profits, 1):
            print(f"Trade {i}: MintBot generated a {profit*100:.2f}% profit.")
            time.sleep(1)  # Simulate some delay between trades
        print("MintBot simulation completed.")
        self.check_trial_status()

    def check_trial_status(self):
        """Check if the trial period has ended for QuantumDeFi (MintBot, VaultBot, PaperBot)."""
        if time.time() - self.start_time > self.free_trial_period:
            self.trial_active = False
            self.prompt_user_for_decision()

    def prompt_user_for_decision(self):
        """Prompt the user with unified QuantumDeFi subscription options."""
        print("\n🚀 Your QuantumDeFi free trial is about to expire! Please choose an option:")
        time.sleep(1)  # Simulate a slight delay for user experience
        print("\n✨ With QuantumDeFi, you’ll unlock exclusive features with VaultBot.")
        time.sleep(1)  # Simulate a slight delay for user experience
        print("🔥 You could have earned even more with VaultBot’s automated risk management and advanced DeFi strategies.")
        time.sleep(1)  # Simulate a slight delay for user experience

        choice = input("\nDo you want to 1) Extend QuantumDeFi Subscription or 2) Exit? Enter 1 or 2: ")

        if choice == '1':
            # Apply early bird discount if subscribed during the trial
            self.apply_early_bird_discount()
            self.offer_subscription_options()
        elif choice == '2':
            print("Thank you for using the QuantumDeFi free trial. You have 7 days to return for a 10% discount!")
            # Set a date 7 days from trial end where the return discount will expire
            self.discount_eligible_until = datetime.now() + self.return_discount_window
        else:
            print("Invalid choice! Please try again.")
            self.prompt_user_for_decision()

    def apply_early_bird_discount(self):
        """Apply a 15% early bird discount if subscribed during the free trial."""
        print("\n🎉 Early Bird Discount Applied: You’ll receive a 15% discount on any QuantumDeFi subscription!")

    def check_return_discount(self):
        """Check if the user is eligible for a 10% return discount within 7 days after trial completion."""
        if self.discount_eligible_until and datetime.now() <= self.discount_eligible_until:
            print("\n🎉 Welcome back! You are eligible for a 10% return discount on any QuantumDeFi subscription.")
            return True
        else:
            print("\nSorry, your 10% return discount has expired.")
            return False

    def offer_subscription_options(self):
        """Offer subscription options for QuantumDeFi with possible discounts."""
        if self.check_return_discount():
            discount = 0.10  # 10% discount for return users
        else:
            discount = 0.0  # No discount if return window expired

        print("\nQuantumDeFi Subscription Options:")
        print(f"1. 30 days for ${30 * (1 - discount):.2f}")
        print(f"2. 90 days for ${80 * (1 - discount):.2f}")
        print(f"3. 180 days for ${150 * (1 - discount):.2f}")
        print(f"4. 360 days for ${260 * (1 - discount):.2f}")

        subscription_choice = input("Select your subscription plan (1-4): ")
        self.process_subscription(subscription_choice)

    def process_subscription(self, choice):
        """Process the selected subscription for QuantumDeFi."""
        if choice == '1':
            print("You’ve subscribed to QuantumDeFi for 30 days!")
        elif choice == '2':
            print("You’ve subscribed to QuantumDeFi for 90 days!")
        elif choice == '3':
            print("You’ve subscribed to QuantumDeFi for 180 days!")
        elif choice == '4':
            print("You’ve subscribed to QuantumDeFi for 360 days!")
        else:
            print("Invalid choice! Please try again.")
            self.offer_subscription_options()

# Entry point for running the MintBot simulation
if __name__ == "__main__":
    mint_bot = MintBot()
    mint_bot.run_simulation()
