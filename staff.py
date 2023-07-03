class Staff:

    @staticmethod
    def add_staff(db_connection_cursor, pj_name, designation, rate):
        command = f'INSERT INTO staff_{pj_name} (designation, rate) VALUES (?, ?)'
        db_connection_cursor.execute(command, (designation, rate))
        db_connection_cursor.connection.commit()

    @staticmethod
    def update_staff(db_connection, df, pj_name):
        
        df.to_sql(f'staff_{pj_name}', db_connection, if_exists='replace', index=False, dtype={'staff_id': 'INTEGER PRIMARY KEY AUTOINCREMENT'})