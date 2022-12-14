import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_multyply_calculator_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

 #   def test_multyply_calculator_failed(self):
 #       assert self.calc.multiply(self, 2, 2) == 5

 
