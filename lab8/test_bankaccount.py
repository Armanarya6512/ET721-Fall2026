import unittest
from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Alice", 100)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_withdraw_too_much(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(500)

    def test_deposits_and_withdrawals(self):
        self.account.deposit(50)
        self.account.withdraw(20)
        self.account.deposit(30)
        self.assertEqual(self.account.get_balance(), 160)


if __name__ == "__main__":
    unittest.main()