import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee_1 = Employee("Peter", "Pan", 80_000)
        return
    
    def test_employee_email(self):
        self.assertEqual(self.employee_1.employee_email, "Peter.Pan@workplace.com")

        self.employee_1.first_name = "Will"
        self.assertEqual(self.employee_1.employee_email, "Will.Pan@workplace.com")
        return

    def test_apply_raise(self):
        self.assertEqual(self.employee_1.salary, 80_000)
        self.employee_1.apply_raise()
        self.assertEqual(self.employee_1.salary, 84_000)

if __name__ == "__main__":
    unittest.main()
