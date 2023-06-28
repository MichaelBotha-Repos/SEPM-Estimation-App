class Materials:

    @staticmethod
    def add_material(db_connection_cursor, pj_name, desc, number_required, unit_cost):
        command = f'INSERT INTO material_{pj_name} (description, number_required, unit_cost) VALUES (?, ?, ?)'
        db_connection_cursor.execute(command, (desc, number_required, unit_cost))
        db_connection_cursor.connection.commit()

    @staticmethod
    def update_materials(db_connection, df, pj_name):
        
        print(df)
        df.to_sql(f'material_{pj_name}', db_connection, if_exists='replace', index=False)
    
