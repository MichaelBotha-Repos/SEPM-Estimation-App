"""This progam will implement the Planning Poker methodology of project estimation"""

import sqlite3

class Task:
    """Represents a task"""
    def __init__(self):
        self.task_description = ''
        self.task_estimations = []
        # self.task_dependencies = []
        self.chosen_estimation = 0
        self.add_description()
        self.add_estimations()

    def add_description(self):
        print('Please enter a task description:\n')
        self.task_description = input()

    def add_estimations(self):
        for i in range(5):
            estimate = input(f"Please enter the {i + 1} effort estimation for task in man.hours:\n")
            self.task_estimations.append(estimate)

    def add_dependency(self):
        print('Please enter the ID of the task dependency')
        dependency = input()
        self.task_dependencies.append(dependency)
        

class Project:
    """Represents a project with all allocated tasks and assigned efforts"""
    def __init__(self):
        self.project_id = input('Please insert a project name:\n')
        self.tasks = []

    def add_task(self):
        '''Method for adding a task '''
        self.tasks.append(Task())

    def display_tasks(self):
        print("\nTask Description\tTask Estimation 1\tTask Estimation 2\tTask Estimation 3\tTask Estimation 4\tTask Estimation 5\tChosen Estimation")
        for task in self.tasks:
            print(f"{task.task_description}\t\t\t{task.task_estimations[0]}\t\t\t{task.task_estimations[1]}\t\t\t{task.task_estimations[2]}\t\t\t{task.task_estimations[3]}\t\t\t{task.task_estimations[4]}\t\t\t{task.chosen_estimation}")
            
        print('\n\n')
        
       
        

if __name__ == '__main__':
    # Main control flow of code
    db_connection = sqlite3.connect('estimations.db')
    while True:
        print("Welcome")
        print("Please select and option:")
        print("1 - Create a new project")
        print("2 - Edit an existing project")
        print("3 - Exit")
        choice = input()

        if choice == '1':
            new_project = Project()
            while True:
                print("Please select and option:")
                print("1 - Create a new task")
                print("2 - Edit an existing task")
                print("3 - Display all tasks")
                print("4 - Save Project")
                print("5 - Exit")
                choice2 = input()
                if choice2 == '1':
                    new_project.add_task()
                elif choice2 == '2':
                    pass
                elif choice2 == '3':
                    new_project.display_tasks()
                elif choice2 == '4':
                    db_connection_cursor = db_connection.cursor()
                    command1 = f"CREATE TABLE {new_project.project_id}("
                    command2 = '''TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
                                Task_description TEXT,
                                Estimate1 INTEGER,
                                Estimate2 INTEGER,
                                Estimate3 INTEGER,
                                Estimate4 INTEGER,
                                Estimate5 INTEGER );'''
                    db_connection_cursor.execute(command1+command2)
                    for task in new_project.tasks:
                        db_connection_cursor.execute(f"INSERT INTO {new_project.project_id} (Task_description,Estimate1, Estimate2, Estimate3, Estimate4, Estimate5) VALUES ('{task.task_description}' {', ' + ', '.join(task.task_estimations)})")
                elif choice2 == '5':
                    break

        elif choice == '2':
            pass

        elif choice == '3':
            exit()

