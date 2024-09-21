import unittest
from mint_bot import PaperBot

class TestMintBot(unittest.TestCase):
    def test_initial_balance(self):
        bot = PaperBot(initial_balance=1000)
        self.assertEqual(bot.balance, 1000)

if __name__ == '__main__':
    unittest.main()
