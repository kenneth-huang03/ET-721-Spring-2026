class Employee:
    raise_percentage = 1.05

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        return

    @property
    def employee_email(self):
        return f"{self.first_name}.{self.last_name}@workplace.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percentage)
        return

if __name__ == "__main__":
    employee_1 = Employee("Peter", "Pan", 80_000)
    print(f"Employee Full Name = {employee_1.full_name}")
    print(f"Employee email = {employee_1.employee_email}")
    print(f"Employee salary = ${employee_1.salary}/yr")
    employee_1.apply_raise()
    print(f"Employee salary after raise = ${employee_1.salary}/yr"  )

