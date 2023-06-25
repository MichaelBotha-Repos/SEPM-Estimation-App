from task import Task

class Project:
    """Represents a project with all allocated tasks and assigned efforts, as well as material costs"""
    def __init__(self, db_connection_cursor, new=True):
        self.db_connection_cursor = db_connection_cursor
        if new:
            self.project_id = input('Please insert a project name:\n')
            # Create tables/relations relevant to the project
            print(db_connection_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"))
            table_names = db_connection_cursor.fetchall()
            print(table_names)
            if len(table_names)== 0:
                command = 'CREATE TABLE projects('\
                          'project_id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                          'project_description TEXT );'
                db_connection_cursor.execute(command)

            command = f'CREATE TABLE tasks_{self.project_id}('\
                        'task_id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                        'task_description TEXT,'\
                        'estimate1 INTEGER,'\
                        'estimate2 INTEGER,'\
                        'estimate3 INTEGER,'\
                        'chosen_estimate INTEGER'\
                        'allocated_staff INTEGER );'
            db_connection_cursor.execute(command)
            command = f'CREATE TABLE staff_{self.project_id}('\
                       'staff_id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                       'designation TEXT,'\
                       'rate FLOAT );'
            db_connection_cursor.execute(command)
            command = f'CREATE TABLE material_{self.project_id}('\
                       'material_id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                       'description TEXT,'\
                       'number_required FLOAT,'\
                       'unit_cost FLOAT );'
            db_connection_cursor.execute(command)
            print(db_connection_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"))
            print(db_connection_cursor.fetchall())
            #to add new project to projects tables

        else:
            ...

    def add_task(self):
        '''Method for adding a task '''
        self.tasks.append(Task())

    def display_tasks(self):
        print("\nTask Description\t"
              "Task Estimation 1\t"
              "Task Estimation 2\t"
              "Task Estimation 3\t"
              "Chosen Estimation")
        for task in self.tasks:
            print(f"{task.task_description}\t\t\t"
                  f"{task.task_estimations[0]}\t\t\t"
                  f"{task.task_estimations[1]}\t\t\t"
                  f"{task.task_estimations[2]}\t\t\t"
                  f"{task.chosen_estimation}")
            
        print('\n\n')
        