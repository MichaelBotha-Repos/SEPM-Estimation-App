"""
method used to handle materials records, add and edit them
"""
class Materials:
    """
    adds materials to table
    args: connection cursor, project name, materials fields
    """
    @staticmethod
    def add_material(db_connection_cursor, pj_name, desc, number_required, unit_cost):
        command = f'INSERT INTO material_{pj_name} (description, number_required, unit_cost) VALUES (?, ?, ?)'
        db_connection_cursor.execute(command, (desc, number_required, unit_cost))
        db_connection_cursor.connection.commit()

    """
    method that updates materials records
    args: db connection, dataframe pandas, project name
    """
    @staticmethod
    def update_materials(db_connection, df, pj_name):
        # pandas method to send dataframe to sql table, see pandas docs to_sql section
        df.to_sql(f'material_{pj_name}', db_connection, if_exists='replace', index=False, dtype={'material_id': 'INTEGER PRIMARY KEY AUTOINCREMENT'})
    
