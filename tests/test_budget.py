import unittest
from budget_manager import BUDGET
import pandas as pd
import os

class TestBudgetManager(unittest.TestCase):

    def test_budget_structure(self):
        self.assertIsInstance(BUDGET, dict)
        self.assertIn("Food", BUDGET)
        self.assertGreater(BUDGET["Food"], 0)

if __name__ == '__main__':
    unittest.main()