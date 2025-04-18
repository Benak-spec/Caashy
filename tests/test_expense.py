import unittest
import os
import pandas as pd
from tracker_module import log_expense, EXPENSE_FILE


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        # Backup existing CSV if it exists
        if os.path.exists(EXPENSE_FILE):
            os.rename(EXPENSE_FILE, EXPENSE_FILE + '.bak')

    def tearDown(self):
        # Cleanup after test
        if os.path.exists(EXPENSE_FILE):
            os.remove(EXPENSE_FILE)
        # Restore backup
        if os.path.exists(EXPENSE_FILE + '.bak'):
            os.rename(EXPENSE_FILE + '.bak', EXPENSE_FILE)

    def test_log_expense_creates_file_and_logs(self):
        log_expense(100, 'TestCategory', 'TestNote')
        self.assertTrue(os.path.exists(EXPENSE_FILE))

        df = pd.read_csv(EXPENSE_FILE)
        self.assertFalse(df.empty)
        self.assertIn('TestCategory', df['Category'].values)


if __name__ == '__main__':
    unittest.main()
