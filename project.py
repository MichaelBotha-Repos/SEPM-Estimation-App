import pandas as pd

"""
This class purpose is to handle the creation of a project from a GUI created using streamlit
"""
        
class Project_from_gui:

    """
    This method creates a new project and lists it in the projects table, then creates all the tables necessary for the records

    args: DB connection tool, name of the project
    """
    @staticmethod
    def new_project(db_connection_cursor, name):


        name = name.lower().replace(" ", "_")

        command = 'CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY AUTOINCREMENT, project_name TEXT)'
        db_connection_cursor.execute(command)

        command = 'INSERT INTO projects(project_name)'\
                    'VALUES(?);'
        db_connection_cursor.execute(command, (name,))
        db_connection_cursor.connection.commit()


        command = f'CREATE TABLE tasks_{name}('\
                        'task_id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                        'task_description TEXT,'\
                        'estimate1 INTEGER,'\
                        'estimate2 INTEGER,'\
                        'estimate3 INTEGER,'\
                        'chosen_estimate INTEGER,'\
                        'allocated_staff INTEGER );'
        db_connection_cursor.execute(command)
        command = f'CREATE TABLE staff_{name}('\
                       'staff_id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                       'designation TEXT,'\
                       'rate FLOAT );'
        db_connection_cursor.execute(command)
        command = f'CREATE TABLE material_{name}('\
                       'material_id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                       'description TEXT,'\
                       'number_required FLOAT,'\
                       'unit_cost FLOAT );'
        db_connection_cursor.execute(command)

    @staticmethod
    def delete_project(db_connection_cursor, name):
        command = 'DELETE FROM projects WHERE project_name = ?'
        db_connection_cursor.execute(command, (name,))
        db_connection_cursor.connection.commit()
        


    """
    this method retrieves all the projects created until now in order to display them in the GUI edit page

    args: DB connection tool

    returns: list of projects
    """
    @staticmethod
    def get_projects(db_connection_cursor):
        # SQL command
        command = 'SELECT project_name FROM projects'
        db_connection_cursor.execute(command)

        results = db_connection_cursor.fetchall()
        # makes a list from the sql query
        project_names = [row[0] for row in results]

        return project_names
    
    # method that gets tasks table info
    @staticmethod
    def get_tasks(db_connection_cursor, name):
        #SQL query to get project related tasks
        command = f'SELECT * FROM tasks_{name}'
        db_connection_cursor.execute(command)

        results = db_connection_cursor.fetchall()
        
    # creating a pandas df to display
        df = pd.DataFrame(results, columns=['task_id', 'task_description', 'estimate1', 'estimate2', 'estimate3', 'chosen_estimate', 'allocated_staff'])
        # eliminating the index that conflicts with sql
        df = df.reset_index(drop=True)

        return df
    
    # method that gets materials table info
    @staticmethod
    def get_materials(db_connection_cursor, name):
        command = f'SELECT * FROM material_{name}'
        db_connection_cursor.execute(command)

        results = db_connection_cursor.fetchall()
        

        df = pd.DataFrame(results, columns=['material_id', 'description', 'number_required', 'unit_cost'])

        df = df.reset_index(drop=True)

        return df
    
    # method that gets staff table info
    @staticmethod
    def get_staff(db_connection_cursor, name):
        command = f'SELECT * FROM staff_{name}'
        db_connection_cursor.execute(command)

        results = db_connection_cursor.fetchall()
        

        df = pd.DataFrame(results, columns=['staff_id', 'designation', 'rate'])

        df = df.reset_index(drop=True)

        return df

        
        