from task import Task

class Project:
    """Represents a project with all allocated tasks and assigned efforts, as well as material costs"""
    def __init__(self, db_connection_cursor):
        self.project_id = input('Please insert a project name:\n')
        self.tasks = []
        self.db_connection_cursor = db_connection_cursor

        # Create tables/relations relevant to the project
        command1 = f"CREATE TABLE tasks_{self.project_id}("
        command2 = '''task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      task_description TEXT,
                      estimate1 INTEGER,
                      estimate2 INTEGER,
                      estimate3 INTEGER,
                      chosen_estimate INTEGER
                      allocated_staff INTEGER );'''
        db_connection_cursor.execute(command1+command2)

        command1 = f"CREATE TABLE staff_{self.project_id}("
        command2 = '''staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      designation TEXT,
                      rate FLOAT );'''
        db_connection_cursor.execute(command1+command2)

        command1 = f"CREATE TABLE material_{self.project_id}("
        command2 = '''material_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      description TEXT,
                      number_required FLOAT,
                      unit_cost FLOAT );'''
        db_connection_cursor.execute(command1+command2)

    def add_task(self):
        '''Method for adding a task '''
        self.tasks.append(Task())

    def display_tasks(self):
        print("\nTask Description\tTask Estimation 1\tTask Estimation 2\tTask Estimation 3\tTask Estimation 4\tTask Estimation 5\tChosen Estimation")
        for task in self.tasks:
            print(f"{task.task_description}\t\t\t{task.task_estimations[0]}\t\t\t{task.task_estimations[1]}\t\t\t{task.task_estimations[2]}\t\t\t{task.task_estimations[3]}\t\t\t{task.task_estimations[4]}\t\t\t{task.chosen_estimation}")
            
        print('\n\n')
        