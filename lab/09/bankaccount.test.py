import unittest

from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccount("test-account", 0)
        return

    def test_deposit(self):
        self.assertEqual(self.bank_account.get_balance(), 0)

        self.assertIsNone(self.bank_account.deposit(19))
        self.assertEqual(self.bank_account.get_balance(), 19)

        self.assertIsNone(self.bank_account.deposit(41))
        self.assertEqual(self.bank_account.get_balance(), 60)

        with self.assertRaises(ValueError):
            self.bank_account.deposit(0)
            self.assertEqual(self.bank_account.get_balance(), 60)

            self.bank_account.deposit(-50)
            self.assertEqual(self.bank_account.get_balance(), 60)

        return 

    def test_withdraw(self):
        self.assertEqual(self.bank_account.get_balance(), 0)
        
        self.assertIsNone(self.bank_account.deposit(50))
        self.assertEqual(self.bank_account.get_balance(), 50)

        self.assertIsNone(self.bank_account.withdraw(1))
        self.assertEqual(self.bank_account.get_balance(), 49)

        self.assertIsNone(self.bank_account.withdraw(48))
        self.assertEqual(self.bank_account.get_balance(), 1)

        with self.assertRaises(ValueError):
            self.bank_account.withdraw(2)
            self.assertEqual(self.bank_account.get_balance(), 1)

            self.bank_account.withdraw(0)
            self.assertEqual(self.bank_account.get_balance(), 1)

            self.bank_account.withdraw(-30)
            self.assertEqual(self.bank_account.get_balance(), 1)

        return


if __name__ == "__main__":
    unittest.main()
