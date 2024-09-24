import sys
import os

# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MintBot.mint_bot import MintBot
from VaultBot.vault_bot import VaultBot

# PaperBot class definition
class PaperBot:
    def toggle_bot(self, bot_type="1"):
        if bot_type == "1":
            print("\n🪙 MintBot activated: Aggressive market seizing strategy!")
            self.active_bot = MintBot()
        elif bot_type == "2":
            print("\n🔐 VaultBot activated: Conservative, risk-managed strategy!")
            self.active_bot = VaultBot()
        else:
            print("Invalid choice! Please pick '1' for MintBot or '2' for VaultBot.")
            self.active_bot = None

    def run_simulation(self):
        """Run the active bot's simulation (MintBot or VaultBot)."""
        if self.active_bot:
            self.active_bot.run_simulation()
        else:
            print("No bot selected. Please toggle to either MintBot or VaultBot.")

if __name__ == "__main__":
    # Create an instance of PaperBot and allow the user to select the bot
    paper_bot = PaperBot()
    print("Pick your strategy:")
    print("1. Aggressive MintBot (high-risk, high-reward)")
    print("2. Conservative VaultBot (low-risk, steady profit using DeFi protocols)")

    user_choice = input("Enter '1' for MintBot or '2' for VaultBot: ")
    paper_bot.toggle_bot(user_choice)
    paper_bot.run_simulation()
