import pandas as pd
import logging


class Task:
    """
    this class is used to manage tasks, add and edit them
    """

    def __init__(self):
        self.task_description = ''
        self.task_estimations = []
        self.chosen_estimation = 0
        self.add_description()
        self.add_estimations()

    def add_description(self):
        print('Please enter a task description:\n')
        self.task_description = input()

    def add_estimations(self):
        for i in range(3):
            estimate = input(f"Please enter the {i + 1} effort estimation for task in man.hours:\n")
            self.task_estimations.append(int(estimate))

    def add_chosen_estimation(self):
        self.chosen_estimation = int(input("\nPlease enter your chosen estimate:\n"))

    """
    This method is used to add a single task to the DB
    args: connection cursor, project name, task DB fields
    """

    @staticmethod
    def add_task(db_cursor, project_name, desc, est_1, est_2, est_3, chosen_est, staff):
        # SQL command
        try:
            command = f"INSERT INTO tasks_{project_name} (task_description, estimate1, estimate2, estimate3, " \
                      f"chosen_estimate, allocated_staff) VALUES (?, ?, ?, ?, ?, ?) "
            values = (desc, est_1, est_2, est_3, chosen_est, staff)
            db_cursor.execute(command, values)
            db_cursor.connection.commit()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            db_cursor.connection.rollback()

    """
    This method updates the task table using a pandas df
    args: db connection (not cursor), dataframe, project name (to get table)
    """

    @staticmethod
    def update_tasks(db_cursor, df, project_name):
        # pandas method to send dataframe to sql table see panda docs to_sql section
        try:
            db_cursor.connection.begin()
            df.to_sql(f'tasks_{project_name}', db_cursor.connection, if_exists='replace', index=False,
                      dtype={'task_id': 'INTEGER PRIMARY KEY AUTOINCREMENT'})
            db_cursor.connection.commit()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            db_cursor.connection.rollback()

    """
    method to delete task

    args: DB connection cursor, project name, task id
    """

    @staticmethod
    def delete_task(db_cursor, project_name, task_id):
        try:
            command = f"DELETE FROM tasks_{project_name} WHERE task_id = ?"
            db_cursor.execute(command, (task_id,))
            db_cursor.connection.commit()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            db_cursor.connection.rollback()

