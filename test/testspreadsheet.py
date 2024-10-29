from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1.5")
        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple")
        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_formula_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_formula_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_formula_evaluate_invalid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple")
        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_formula_reference_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", 42)
        self.assertEqual(42, spreadsheet.evaluate("A1"))

    def test_formula_reference_invalid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", 42.5)
        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_formula_reference_circular(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

    def test_formula_addition_valid(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3")
        self.assertEqual(4, spreadsheet.evaluate("A1"))

    def test_formula_addition_invalid(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3.5")
        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_formula_division_by_zero(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1/0")
        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_formula_addition_and_multiplication_valid(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3*2")
        self.assertEqual(7, spreadsheet.evaluate("A1"))

    def test_formula_reference_addition_valid(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+B1")
        spreadsheet.set("B1", "=3")
        self.assertEqual(4, spreadsheet.evaluate("A1"))

    def test_formula_reference_addition_invalid(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+B1")
        spreadsheet.set("B1", "=3.1")
        self.assertEqual("#ERROR", spreadsheet.evaluate("A1"))

    def test_formula_reference_addition_circular(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+B1")
        spreadsheet.set("B1", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

    






