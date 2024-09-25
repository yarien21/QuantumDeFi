# Step 1: Define the global toggle for paper trading
PAPER_TRADING = True  # Default is Paper Trading mode

# Step 2: Create a function to handle user selection of bot and trading mode
def show_bot_options():
    print("Select a bot:")
    print("1. MintBot - Money minting 24/7 aggressively to capture the trends every which way to make profit with dynamic risk adjustment and customizable to user needs.")
    print("2. VaultBot - Conservative, yet captures profitable trends 24/7 using low-risk trading strategies and generates passive-income to its user. Customizable.")
    
    bot_choice = int(input("Enter '1' for MintBot or '2' for VaultBot: "))
    
    if bot_choice == 1:
        print("You have selected MintBot.")
        return "mint"
    elif bot_choice == 2:
        print("You have selected VaultBot.")
        return "vault"
    else:
        print("Invalid choice.")
        return show_bot_options()

# Step 3: Handle trading mode (Paper vs. Real Trading)
def set_trading_mode():
    global PAPER_TRADING
   
def main():
    print("UnifiedBot script has started.")
    bot = show_bot_options()  # Select MintBot or VaultBot
    set_trading_mode()  # Paper vs. Real Trading confirmation
    print(f"Selected Bot: {bot}")
    print(f"Trading Mode: {'Paper Trading' if PAPER_TRADING else 'Real Trading'}")

if __name__ == "__main__":
    main()

    