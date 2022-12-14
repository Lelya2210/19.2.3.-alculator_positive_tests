import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_multyply_calculator_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculator_correctly(self):
        assert self.calc.division(self, 24, 8) == 3

    def test_subtraction_calculator_correctly(self):
        assert self.calc.subtraction(self, 24, 8) == 16

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 5, 3) == 8
 
