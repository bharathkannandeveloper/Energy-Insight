import unittest
from unittest.mock import patch
from io import StringIO
from main import admin_login

class TestAdminLogin(unittest.TestCase):

    @patch('builtins.input', side_effect=['existing_admin', 'correct_password'])
    def test_successful_login(self, mock_input):
        # Redirect stdout to capture print statements
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            admin_login()

        # Get the printed output
        output = mock_stdout.getvalue().strip()

        # Assert that the output contains the success message
        self.assertIn("Login successful.", output)

    @patch('builtins.input', side_effect=['nonexistent_admin', 'new_password'])
    def test_failed_login_and_registration(self, mock_input):
        # Redirect stdout to capture print statements
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            admin_login()

        # Get the printed output
        output = mock_stdout.getvalue().strip()

        # Assert that the output contains the failure and registration messages
        self.assertIn("Login failed. Please check your username and password.", output)
        self.assertIn("Admin Registration:", output)
        self.assertIn("Exiting the application. Goodbye!", output)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
