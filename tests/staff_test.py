import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest import mock
from unittest.mock import MagicMock
import logging
from staff import Staff



class StaffTestCase(unittest.TestCase):

    def setUp(self):
        self.db_cursor_mock = MagicMock()
        self.df_mock = MagicMock()

    def test_add_staff_success(self):
        self.db_cursor_mock.execute.return_value = None
        self.db_cursor_mock.connection.commit.return_value = None

        Staff.add_staff(self.db_cursor_mock, "project_1", "Manager", 100)

        self.db_cursor_mock.execute.assert_called_once_with(
            'INSERT INTO staff_project_1 (designation, rate) VALUES (?, ?)',
            ("Manager", 100)
        )
        self.db_cursor_mock.connection.commit.assert_called_once()

    def test_add_staff_exception(self):
        self.db_cursor_mock.execute.side_effect = Exception("DB error")
        self.db_cursor_mock.connection.rollback.return_value = None

        with self.assertRaises(Exception):
            Staff.add_staff(self.db_cursor_mock, "project_1", "Manager", 100)

        self.db_cursor_mock.execute.assert_called_once_with(
            'INSERT INTO staff_project_1 (designation, rate) VALUES (?, ?)',
            ("Manager", 100)
        )
        self.db_cursor_mock.connection.rollback.assert_called_once()

    def test_update_staff_success(self):
        self.df_mock.to_sql.return_value = None

        Staff.update_staff(self.db_cursor_mock, self.df_mock, "project_1")

        self.df_mock.to_sql.assert_called_once_with(
            'staff_project_1', self.db_cursor_mock, if_exists='replace', index=False,
            dtype={'staff_id': 'INTEGER PRIMARY KEY AUTOINCREMENT'}
        )

    def test_update_staff_exception(self):
        self.df_mock.to_sql.side_effect = Exception("DB error")
        self.db_cursor_mock.connection.rollback.return_value = None

        with self.assertRaises(Exception) as context:
            Staff.update_staff(self.db_cursor_mock, self.df_mock, "project_1")

        self.assertEqual(str(context.exception), "DB error")
        self.df_mock.to_sql.assert_called_once_with(
            'staff_project_1', self.db_cursor_mock, if_exists='replace', index=False,
            dtype={'staff_id': 'INTEGER PRIMARY KEY AUTOINCREMENT'}
        )
        self.db_cursor_mock.connection.rollback.assert_called_once()

    def test_delete_staff_success(self):
        self.db_cursor_mock.execute.return_value = None
        self.db_cursor_mock.connection.commit.return_value = None

        Staff.delete_staff(self.db_cursor_mock, "project_1", 1)

        self.db_cursor_mock.execute.assert_called_once_with(
            "DELETE FROM staff_project_1 WHERE staff_id == 1"
        )
        self.db_cursor_mock.connection.commit.assert_called_once()

    def test_delete_staff_exception(self):
        self.db_cursor_mock.execute.side_effect = Exception("DB error")
        self.db_cursor_mock.connection.rollback.return_value = None

        with self.assertRaises(Exception):
            Staff.delete_staff(self.db_cursor_mock, "project_1", 1)

        self.db_cursor_mock.execute.assert_called_once_with(
            "DELETE FROM staff_project_1 WHERE staff_id == 1"
        )
        self.db_cursor_mock.connection.rollback.assert_called_once()


if __name__ == '__main__':
    unittest.main()
