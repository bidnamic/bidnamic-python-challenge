from .connect import db_connect


def create_table(cur, dataset):
    '''
    Run queries to establish if required tables currently exist.
    If they don't exist, create them.
    '''

    # Search for database table, create if it doesn't exist.
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
    if result == 0:
        print('Table does not exist, now creating.')
        # Create table for current dataset.
        cur.execute(dataset.create_table)
    elif result == 1:
        print('Table exists.')
        pass  # One instance of table already exists.


def populate_table(cur, dataset):
    '''
    Check if tables are empty.
    If not empty, clear current dataset in table.
    Else populate with supplied dataset.
    '''

    # Get number of records in current dataset table.
    print(f'Checking if table contains data: {dataset.name}')
    cur.execute(
        f'''
        SELECT COUNT(*)
        FROM {dataset.name}
        '''
    )
    # Returns tuple, assign first element to variable.
    # Result will be int, number of found instances. (Expected 0 or number in supplied data.)
    result = cur.fetchone()[0]
    # If table is not empty.
    if result != 0:
        print('Table not empty, now clearing.')
        # Clear table.
        cur.execute(
            f'''
            DELETE FROM {dataset.name}
            '''
        )
    elif result == 0:
        print('Table is currently empty.')

    # Populate table with current dataset.
    print('Populating table with current dataset.')
    cur.execute(
        f'''
        COPY {dataset.name} ({dataset.fields})
        FROM '{dataset.path}'
        DELIMITER ','
        CSV HEADER
        '''
    )


def ingest(datasets):
    '''
    Connects to database using information in 'database.ini'.
    Checks if required tables exist in database.
    Creates tables if necessary.
    Checks if tables already contain data.
    Clears existing data.
    Populates with supplied datasets.
    '''

    # Create connection using db_connect() function.
    _ = db_connect()
    conn = _[0]  # Connecton.
    cur = _[1]  # Cursor.

    for dataset in datasets:
        # Create required tables within database.
        # Pass cursor to allow create_tables() to use created connection.
        create_table(cur, dataset)

        # Use supplied data files to populate equivilant table entries.
        populate_table(cur, dataset)

    # Run all SQL queries.
    conn.commit()

    # Exit cursor, close connection.
    cur.close()
    conn.close()
