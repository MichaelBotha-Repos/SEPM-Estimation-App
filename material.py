import logging

"""
method used to handle materials records, add and edit them
"""


class Materials:
    """
    adds materials to table
    args: connection cursor, project name, materials fields
    """

    @staticmethod
    def add_material(db_cursor, project_name, desc, number_required, unit_cost):
        try:
            command = f"INSERT INTO material_{project_name} (description, number_required, unit_cost) VALUES (?, ?, ?)"
            values = (desc, number_required, unit_cost)
            db_cursor.execute(command, values)
            db_cursor.connection.commit()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            db_cursor.connection.rollback()

    """
    method that updates materials records
    args: db connection, dataframe pandas, project name
    """

    @staticmethod
    def update_materials(db_connection, df, project_name):
        try:
            # pandas method to send dataframe to sql table, see pandas docs to_sql section
            df.to_sql(f"material_{project_name}", db_connection, if_exists='replace', index=False,
                      dtype={'material_id': 'INTEGER PRIMARY KEY AUTOINCREMENT'})
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            db_connection.rollback()

    @staticmethod
    def delete_material(db_cursor, project_name, material_id):
        try:
            command = f"DELETE FROM material_{project_name} WHERE material_id = ?"
            db_cursor.execute(command, (material_id,))
            db_cursor.connection.commit()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            db_cursor.connection.rollback()
