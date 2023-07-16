import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch
import pandas as pd
import sqlite3
from io import StringIO
from task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task()

    def tearDown(self):
        pass

    def test_add_description(self):
        with patch('builtins.input', return_value='Task description'):
            self.task.add_description()
        self.assertEqual(self.task.task_description, 'Task description')

    def test_add_estimations(self):
        with patch('builtins.input', side_effect=['1', '2', '3']):
            self.task.add_estimations()
        self.assertEqual(self.task.task_estimations, [1, 2, 3])

    def test_add_chosen_estimation(self):
        with patch('builtins.input', return_value='2'):
            self.task.add_chosen_estimation()
        self.assertEqual(self.task.chosen_estimation, 2)

    def test_add_task(self):
        # Connect to an in-memory SQLite database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        project_name = 'TestProject'
        desc = 'Task description'
        est_1, est_2, est_3 = 1, 2, 3
        chosen_est = 2
        staff = 'John Doe'

        Task.add_task(cursor, project_name, desc, est_1, est_2, est_3, chosen_est, staff)

        # Retrieve the inserted task from the database
        cursor.execute(f"SELECT * FROM tasks_{project_name}")
        result = cursor.fetchall()

        expected_result = [(1, desc, est_1, est_2, est_3, chosen_est, staff)]
        self.assertEqual(result, expected_result)

        # Clean up
        conn.close()

    def test_update_tasks(self):
        # Connect to an in-memory SQLite database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        project_name = 'TestProject'

        # Create a sample DataFrame
        data = {
            'task_id': [1, 2, 3],
            'task_description': ['Task 1', 'Task 2', 'Task 3'],
            'estimate1': [1, 2, 3],
            'estimate2': [2, 4, 6],
            'estimate3': [3, 6, 9],
            'chosen_estimate': [2, 4, 6],
            'allocated_staff': ['John', 'Jane', 'Bob']
        }
        df = pd.DataFrame(data)

        Task.update_tasks(cursor, df, project_name)

        # Retrieve the inserted tasks from the database
        cursor.execute(f"SELECT * FROM tasks_{project_name}")
        result = cursor.fetchall()

        expected_result = [(1, 'Task 1', 1, 2, 3, 2, 'John'),
                           (2, 'Task 2', 2, 4, 6, 4, 'Jane'),
                           (3, 'Task 3', 3, 6, 9, 6, 'Bob')]
        self.assertEqual(result, expected_result)

        # Clean up
        conn.close()

    def test_delete_task(self):
        # Connect to an in-memory SQLite database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        project_name = 'TestProject'
        task_id = 1

        # Insert a sample task into the database
        cursor.execute(f"INSERT INTO tasks_{project_name} (task_id) VALUES (?)", (task_id,))
        conn.commit()

        Task.delete_task(cursor, project_name, task_id)

        # Retrieve the remaining tasks from the database
        cursor.execute(f"SELECT * FROM tasks_{project_name}")
        result = cursor.fetchall()

        expected_result = []
        self.assertEqual(result, expected_result)

        # Clean up
        conn.close()


if __name__ == '__main__':
    unittest.main()
