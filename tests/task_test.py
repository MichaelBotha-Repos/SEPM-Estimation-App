import unittest
from unittest.mock import patch
from io import StringIO

import pandas as pd

from task import Task


class TaskTests(unittest.TestCase):
    def test_add_description(self):
        task = Task()
        with patch('builtins.input', return_value='Test Description'):
            task.add_description()
        self.assertEqual(task.task_description, 'Test Description')

    def test_add_estimations(self):
        task = Task()
        with patch('builtins.input', side_effect=['1', '2', '3']):
            task.add_estimations()
        self.assertEqual(task.task_estimations, [1, 2, 3])

    def test_add_chosen_estimation(self):
        task = Task()
        with patch('builtins.input', return_value='2'):
            task.add_chosen_estimation()
        self.assertEqual(task.chosen_estimation, 2)

    @patch('sqlite3.Cursor')
    def test_add_task(self, mock_cursor):
        task = Task('Test Description', [1, 2, 3], 2)
        Task.add_task(mock_cursor, 'project_name', task.task_description, task.task_estimations, task.chosen_estimation,
                      'staff_name')
        mock_cursor.execute.assert_called_once_with(
            'INSERT INTO tasks_project_name (task_description, estimate1, estimate2, estimate3, chosen_estimate, '
            'allocated_staff) VALUES (?, ?, ?, ?, ?, ?)',
            ('Test Description', 1, 2, 3, 2, 'staff_name')
        )

    @patch('pandas.DataFrame.to_sql')
    def test_update_tasks(self, mock_to_sql):
        task = Task('Test Description', [1, 2, 3], 2)
        df = pd.DataFrame({'task_id': [1, 2, 3]})
        Task.update_tasks('db_connection', df, 'project_name')
        mock_to_sql.assert_called_once_with(
            'tasks_project_name',
            'db_connection',
            if_exists='replace',
            index=False,
            dtype={'task_id': 'INTEGER PRIMARY KEY AUTOINCREMENT'}
        )

    @patch('sqlite3.Cursor')
    def test_delete_task(self, mock_cursor):
        Task.delete_task(mock_cursor, 'project_name', 123)
        mock_cursor.execute.assert_called_once_with(
            'DELETE FROM tasks_project_name WHERE task_id == 123'
        )


if __name__ == '__main__':
    unittest.main()
