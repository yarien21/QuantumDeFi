# mint_bot.py
# import time
import numpy as np
import time

# Define the MintBot class
class MintBot:
    def __init__(self):
        self.start_time = time.time()
        self.free_trial_period = 36 * 3600  # 36 hours in seconds
        self.trial_active = True

    def run(self):
        while self.trial_active:
            # Simulate the bot running
            time.sleep(5)  # Placeholder for activity
            self.check_trial_status()

    def check_trial_status(self):
        """Check if the trial period has ended."""
        if time.time() - self.start_time > self.free_trial_period:
            self.trial_active = False
            self.prompt_user_for_decision()

    def prompt_user_for_decision(self):
        """Prompt the user with choices once the trial is over."""
        print("\n🚀 Your free trial is about to expire!")
        time.sleep(1)
        print("\n✨ With VaultBot, you’ll unlock exclusive features like staking, farming, and multi-asset strategies.")
        time.sleep(1)
        print("🔥 You could have earned even more with VaultBot strategies and VaultBot’s automated risk management.")
        time.sleep(1)

        choice = input("\nDo you want to 1) Extend MintBot or 2) Subscribe to VaultBot? Enter 1 or 2: ")

        if choice == '1':
            print("\nLimited-time offer: Extend MintBot!")
            print("1. Extend 4 days for $5")
            print("2. Extend 7 days for $10")
            print("3. Extend 21 days for $30")
            extend_choice = input("Select your extension: ")
            self.process_extension(extend_choice)
        elif choice == '2':
            print("\nSubscribe to VaultBot enhanced with cutting-edge DeFi and Blockchain technologies while you get access to staking, farming, and MintBot is inclusive free till promo lasts!")
            print("1. Subscribe for 30 days for $30")
            print("2. Subscribe for 90 days for $75")
            print("3. Subscribe for 180 days for $150")
            print("4. Subscribe for 360 days for $280")
            subscription_choice = input("Select your subscription plan: ")
            self.process_subscription(subscription_choice)
        else:
            print("Invalid choice! Please try again.")
            self.prompt_user_for_decision()

    def process_extension(self, choice):
        """Process the selected extension."""
        if choice == '1':
            print("\nYou’ve extended MintBot for 4 days!")
        elif choice == '2':
            print("\nYou’ve extended MintBot for 7 days!")
        elif choice == '3':
            print("\nYou’ve extended MintBot for 21 days!")
        else:
            print("Invalid choice! Please try again.")
            self.offer_extension_options()

    def process_subscription(self, choice):
        """Process the selected subscription for VaultBot."""
        if choice == '1':
            print("\nYou’ve subscribed to VaultBot for 30 days!")
        elif choice == '2':
            print("\nYou’ve subscribed to VaultBot for 90 days!")
        elif choice == '3':
            print("\nYou’ve subscribed to VaultBot for 180 days!")
        elif choice == '4':
            print("\nYou’ve subscribed to VaultBot for 360 days!")
        else:
            print("Invalid choice! Please try again.")
            self.offer_subscription_options()

    def offer_extension_options(self):
        """Offer extension options for MintBot."""
        print("1. Extend MintBot for 4 days for $5")
        print("2. Extend MintBot for 7 days for $10")
        print("3. Extend MintBot for 21 days for $30")
        extend_choice = input("Select your extension: ")
        self.process_extension(extend_choice)

    def offer_subscription_options(self):
        """Offer subscription options for VaultBot."""
        print("1. Subscribe to VaultBot for 30 days for $30")
        print("2. Subscribe to VaultBot for 90 days for $75")
        print("3. Subscribe to VaultBot for 180 days for $150")
        print("4. Subscribe to VaultBot for 360 days for $280")
        subscription_choice = input("Select your subscription plan: ")
        self.process_subscription(subscription_choice)

    def process_extension(self, choice):
        """Process the selected extension."""
        if choice == '1':
            print("You’ve extended MintBot for 4 days!")
        elif choice == '2':
            print("You’ve extended MintBot for 7 days!")
        elif choice == '3':
            print("You’ve extended MintBot for 21 days!")
        else:
            print("Invalid choice! Please try again.")
            self.offer_extension_options()

    def process_subscription(self, choice):
        """Process the selected subscription for VaultBot."""
        if choice == '1':
            print("You’ve subscribed to VaultBot for 30 days!")
        elif choice == '2':
            print("You’ve subscribed to VaultBot for 90 days!")
        elif choice == '3':
            print("You’ve subscribed to VaultBot for 180 days!")
        elif choice == '4':
            print("You’ve subscribed to VaultBot for 360 days!")
        else:
            print("Invalid choice! Please try again.")
            self.offer_subscription_options()

