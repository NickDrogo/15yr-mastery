import pytest

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount
        return self.annual_salary
    

@pytest.fixture
def custom_raise():
    custom_raise = Employee("john", "Doe", 50000)
    return custom_raise

def test_give_default_raise(custom_raise):
    full_details = custom_raise.give_raise()
    assert  full_details == 55000

def test_give_custom_raise(custom_raise):
    full_details = custom_raise.give_raise(10000)
    assert  full_details == 60000


