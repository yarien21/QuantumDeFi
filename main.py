# main.py
from paper_bot import PaperBot
from vault_bot import VaultBot

def main():
    print("Select Bot:")
    print("1. PaperBot (Simulated Trading)")
    print("2. VaultBot (Live Trading)")

    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        bot = PaperBot()
        bot.run_simulation()
    elif choice == '2':
        bot = VaultBot()
        # Example trade for VaultBot (live trading)
        bot.trade('bitcoin', 50000, 49000)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()


