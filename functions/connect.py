import psycopg2
from configparser import ConfigParser


def db_params(filename='database.ini', section='postgresql'):
    '''
    Gather required information for connecting to database.
    filename = path/to/database.ini
    section = section within database.ini [postgresql]

    Returns para_dict, a dictionary containing: host, port, database name, username, password.
    '''

    # Create parser, read contents of file.
    parser = ConfigParser()
    parser.read(filename)

    # From section, parse information.
    para_dict = {}
    if parser.has_section(section):
        section_parameters = parser.items(section)
        for parameter in section_parameters:
            para_dict[parameter[0]] = parameter[1]
    else:
        raise Exception(f'[{filename}] does not contain [{section}].')

    return para_dict


def db_connect():
    '''
    Create a connection to database using information from database.ini.
    Connection returned as 'cur'. (Cursor.)
    '''

    # Use returned dictionary from db_params() as parameters for connection.
    conn = psycopg2.connect(**db_params())
    # Establish database connection.
    cur = conn.cursor()
    # Return connection and cursor for use.
    return conn, cur
