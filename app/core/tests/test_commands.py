"""
Test custom django management commands.
"""
from psycopg2 import OperationalError as Psycopg2Error
from unittest.mock import patch
from django.test import SimpleTestCase
from django.db.utils import OperationalError
from django.core.management import call_command

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test Commands."""
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if db is ready."""
        patched_check.return_value = True
        
        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, pathced_sleep, patched_check):
        """Test waiting for db if db is not ready."""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(database=['default'])