import logging

"""
This class is used to manage staff records, add and edit them
"""


class Staff:
    """
    add a record to the staff table
    args: connection cursor, project name, material table fields
    """

    @staticmethod
    def add_staff(db_cursor, project_name, designation, rate):
        try:
            command = f'INSERT INTO staff_{project_name} (designation, rate) VALUES (?, ?)'
            db_cursor.execute(command, (designation, rate))
            db_cursor.connection.commit()
        except Exception as e:
            logging.error(f"An error occurred: {e} {project_name} ")
            db_cursor.connection.rollback()

    """
    method used to edit the staff table
    args: connection to db (not cursor, pd dataframe, project name)
    """

    @staticmethod
    def update_staff(db_cursor, df, project_name):
        # pandas method to send a dataframe to sql, see pandas docs to_sql section
        try:
            df.to_sql(f'staff_{project_name}', db_cursor, if_exists='replace', index=False,
                      dtype={'staff_id': 'INTEGER PRIMARY KEY AUTOINCREMENT'})
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            db_cursor.connection.rollback()

    """
    delete a record from the staff table
    args: DB connection cursor, project name and staff id
    """

    @staticmethod
    def delete_staff(db_cursor, project_name, staff_id):
        try:
            command = f"DELETE FROM staff_{project_name} WHERE staff_id == {staff_id}"
            db_cursor.execute(command)
            db_cursor.connection.commit()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            db_cursor.connection.rollback()
