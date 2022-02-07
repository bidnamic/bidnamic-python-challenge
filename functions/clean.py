from .connect import db_connect


def clean(datasets):
    '''
    Removes tables created by this script from database.
    '''

    # Create connection using db_connect() function.
    _ = db_connect()
    conn = _[0]  # Connecton.
    cur = _[1]  # Cursor.

    for dataset in datasets:
        # Establish if table exists.
        print(f'Checking if table exists: {dataset.name}')
        cur.execute(
            f'''
            SELECT COUNT(*) FROM information_schema.tables
            WHERE table_name = '{dataset.name}'
            '''
        )

        # Returns tuple, assign first element to variable.
        # Result will be int, number of found instances. (Expected 0 or 1.)
        result = cur.fetchone()[0]
        # If there are zero results when searching for table.
        if result == 1:
            print(f'Now dropping table: {dataset.name}')
            cur.execute(
                f'''
                DROP TABLE {dataset.name}
                '''
            )
        elif result == 0:
            print('Table does not exist.')
            pass

    # Run all SQL queries.
    conn.commit()

    # Exit cursor, close connection.
    cur.close()
    conn.close()
