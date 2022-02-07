from .connect import db_connect
from prettytable import PrettyTable as pt


def query(query, *quantity):
    '''
    Takes passed argument with optional additional argument for quantity.
    Prints out top number of search terms for passed query and quantity.
    '''

    # Take optional quantity argument if passed, else default to 10.
    if quantity:
        quantity = quantity[0]
    else:
        quantity = 10

    # Create connection using db_connect() function.
    _ = db_connect()
    conn = _[0]  # Connecton.
    cur = _[1]  # Cursor.

    cur.execute(
        f'''
        SELECT search_term as "Search term", round(conversion_value/cost, 2) as "ROAS", adgroups.campaign_id as "Campaign ID"
        FROM search_terms
        INNER JOIN adgroups using (campaign_id)
        WHERE conversion_value != 0
        AND adgroups.alias LIKE '%{query}%'
        GROUP BY "Search term", "ROAS", "Campaign ID"
        ORDER BY "ROAS" desc
        LIMIT {quantity};
        '''
    )
    raw_results = cur.fetchall()

    # Table headings.
    results = pt(['Search term', 'ROAS', 'Campaign ID'])
    # Column alignment.
    results.align['Search term'] = 'l'
    results.align['ROAS'] = 'r'
    results.align['Campaign ID'] = 'r'

    # Map decimal returns into strings, append to results table.
    for raw_result in raw_results:
        results.add_row(list(map(str, list(raw_result))))

    print(results)

    # Exit cursor, close connection.
    cur.close()
    conn.close()
