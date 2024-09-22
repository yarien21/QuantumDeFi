import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'MintBot')))  # Add MintBot to sys path

from mint_bot import MintBot  # Import MintBot correctly
from vault_bot import VaultBot

class BotPricing:
    def __init__(self):
        self.vaultbot_price = 30  # Assume $30 per month for VaultBot
        self.mintbot_future_price = 28  # Assume $28 per month for MintBot after promo
        self.current_promo = True  # Promo status for MintBot

    def calculate_savings(self):
        # Calculate cost savings by choosing VaultBot over MintBot after promo
        return self.mintbot_future_price - self.vaultbot_price

    def display_pricing_info(self):
        if self.current_promo:
            print("Promo: MintBot is currently FREE for a limited time!")
        print(f"VaultBot Subscription: ${self.vaultbot_price} per month.")
        print(f"MintBot will cost ${self.mintbot_future_price} per month after the promo ends.")
        print(f"Save ${self.calculate_savings()} per month by subscribing to VaultBot now!")

def main():
    pricing = BotPricing()
    
    print("Select Bot:")
    print("1. MintBot (Simulated Trading)")
    print("2. VaultBot (Live Trading)")
    pricing.display_pricing_info()  # Display the pricing info, promo, and savings

    choice = input("Enter choice (1 or 2): ")
    print(f"Choice entered: {choice}")

    if choice == '1':
        if pricing.current_promo:
            print("MintBot is FREE during the promo!")
        bot = MintBot()  # Use MintBot for simulation
        bot.run_simulation()  # Run simulation
    elif choice == '2':
        bot = VaultBot(initial_balance=50000)  # Use VaultBot for live trading
        bot.execute_trade()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()


# can you help me improve this code?
# MintBot should do conversion for us. 
 #   People come in for free for three days. That three day experiences should be extraordinaly. Provide them the very exclusive experience such that they cant walk away. They get the same super literally generating profit. MintBot is to be topnotch. We only tease them to experience the money minting experience for three days absolutely free. However, After 36hours, they need to make desicion either they continue or quit. If they continue, they have two choices. Choice one: Extend MintBot trade for next 4 days for $5. or they can extend for 7 days for $10. or 21 days for $30. Choice 2: They subscribe for VaultBot for monthly subscription. For 30 days: $30, for 90 days: $75, for 180days: $150, for 360 days: $280. with free paper trading with MintBot. We do not want to have a pro membership because our MintBot is a more than a super pro. We cannot downgrade after exclusive MintBot user experience because they feel assured and confident enough to hop on to VaultBot journey without hesitation. Hence, we need to give them the ditto experience. Please comment.

  # MintBot should do conversion for us. 
#   People come in for free for three days. That three day experiences should be extraordinaly. Provide them the very exclusive experience such that they cant walk away. They get the same super literally generating profit. MintBot is to be topnotch. We only tease them to experience the money minting experience for three days absolutely free. However, After 36hours, they need to make desicion either they continue or quit. If they continue, they have two choices. Choice one: Extend MintBot trade for next 4 days for $5. or they can extend for 7 days for $10. or 21 days for $30. Choice 2: They subscribe for VaultBot for monthly subscription. For 30 days: $30, for 90 days: $75, for 180days: $150, for 360 days: $280. with free paper trading with MintBot. We do not want to have a pro membership because our MintBot is a more than a super pro. We cannot downgrade after exclusive MintBot user experience because they feel assured and confident enough to hop on to VaultBot journey without hesitation. Hence, we need to give them the ditto experience. Please comment.

# Our strategy for MintBot is to give its users an irresistible experience during the 36 hour free trial. This experience must convert them into paying customers who feel confident about the MinBot’s capabilities. Here’s a breakdown of the approach and how we can implement it:
Key Points of Your Strategy:
1.	Free 3-Day Trial with Extraordinary Experience: (Requires sign up).
■	Objective: Provide an unbeatable trading experience during the free trial, ensuring users feel they are making real profits and gaining confidence in MintBot's potential. 
■	Full access to full service that includes Staking, Farming, and Pooling. 
■	Approach: MintBot needs to simulate an advanced trading experience that feels premium from the start. The goal is to make the user believe that their profits are legitimate and substantial enough to continue beyond the free trial. 
■	Key Tools: Calculator to calculate estimated profit and Loss over time and amount invested. 
We need to test this feature to determine the probability rate of success maximized.
2.	Decision After 30 Hours: (2 choices) (Credit Card needed).
■	Objective: Create a sense of urgency with a decision prompt after 24 hours.
■	Approach: After 30 hours, provide two clear options:
	Extend the MintBot Experience for an affordable fee with an early bird discount of 8% only for a 21-day MintBot trial.
	OR
	Upgrade to VaultBot for a subscription-based option depending on the type of subscription for continued trading with premium features and a free MintBot subscription for 90 days subscription.
3.	Final Approach at exactly 35.5 hours: (Provide three clear choices) (Credit Card needed)
■	Extend the MintBot Experience. Pick a 4, 7, or 21days from the subscription plan, which will automatically renew unless it is canceled well before expiry.
Or
○	Upgrade to VaultBot, Pick a subscription plan option for continued making real money. 
	Pricing Model for Decision:
○	Choice 1: Extend MintBot:
1.	4 days for $5.
2.	7 days for $10.
3.	21 days for $30.
○	Choice 2: Subscribe to VaultBot:
1.	30 days for $30.
2.	90 days for $75. 	(with free subscription of MintBot till promo ends.)
3.	180 days for $150. 	(with free subscription of MintBot till promo ends.)
4.	360 days for $280. 	(with free subscription of MintBot till promo ends.)
o	Choice 3: Exit MintBot @ 36 hour from time of subscription. 
	Sorry no access and for losing the opportunity to make $$$.
