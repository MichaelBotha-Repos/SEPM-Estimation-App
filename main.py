"""This progam will implement the Planning Poker methodology of project estimation"""
from project import Project
import sqlite3
  

if __name__ == '__main__':
    # Main control flow of code
    db_connection = sqlite3.connect('estimations.db')
    db_connection_cursor = db_connection.cursor()
    while True:
        print("Welcome")
        print("Please select and option:")
        print("1 - Create a new project")
        print("2 - Edit an existing project")
        print("3 - Exit")
        choice = input()

        if choice == '1':
            new_project = Project(db_connection_cursor)
            while True:
                print("Please select an option:")
                print("1 - Add a new task")
                print("2 - Edit an existing task")
                print("3 - Display all tasks")
                print("4 - Add materials")
                print("4 - Edit materials")
                print("4 - Add staff")
                print("4 - Edit staff")
                print("Calculate project costs")
                print("5 - Exit")
                choice2 = input()
                if choice2 == '1':
                    new_project.add_task()
                elif choice2 == '2':
                    pass
                elif choice2 == '3':
                    new_project.display_tasks()
                elif choice2 == '4':
                    for task in new_project.tasks:
                        db_connection_cursor.execute(f"INSERT INTO {new_project.project_id}" \
                                                    "(Task_description,Estimate1, Estimate2, Estimate3, Estimate4, Estimate5)" \
                                                    f"VALUES ('{task.task_description}' {', ' + ', '.join(task.task_estimations)})")
                        
                elif choice2 == '5':
                    break

        elif choice == '2':
            pass

        elif choice == '3':
            exit()

