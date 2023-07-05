"""
This class is used to manage staff records, add and edit them
"""

class Staff:

    """
    add a record to the staff table
    args: connection cursor, project name, material table fields
    """
    @staticmethod
    def add_staff(db_connection_cursor, pj_name, designation, rate):
        command = f'INSERT INTO staff_{pj_name} (designation, rate) VALUES (?, ?)'
        db_connection_cursor.execute(command, (designation, rate))
        db_connection_cursor.connection.commit()

    """
    method used to edit the staff table
    args: connection to db (not cursor, pd dataframe, project name)
    """
    @staticmethod
    def update_staff(db_connection, df, pj_name):
        # pandas method to send a dataframe to sql, see pandas docs to_sql section
        df.to_sql(f'staff_{pj_name}', db_connection, if_exists='replace', index=False, dtype={'staff_id': 'INTEGER PRIMARY KEY AUTOINCREMENT'})

    """
    delete a record from the staff table
    args: DB connection cursor, project name and staff id
    """
    @staticmethod
    def delete_staff(db_connection_cursor, pj_name, staff_id):
        command = f"DELETE FROM staff_{pj_name} WHERE staff_id == {staff_id}"
        db_connection_cursor.execute(command)
        db_connection_cursor.connection.commit()