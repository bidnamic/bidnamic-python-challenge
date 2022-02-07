from .datasets import datasets
from .ingest import ingest
from .clean import clean
from .query import query


def check_args(args):
    '''
    Handles any (if entered) arguments at command line.

    Expected: None      - Runs through functions that 'Import' & 'Query' handle.
              Ingest    - Ingest datasets into database.
              Clean     - Cleans data from database.
              Query (X) - Returns query results.
              (Query also takes takes an optional integer for number of query results.
              Default if none is entered is 10. Maximum is limited to 1,000.)

    Unexpected values will be ignored, will be treated as if no arguments were passed.

    '''

    # No additional arguments passed, one being script name.
    if len(args) == 0:
        print('No arguments passed, see README.')

    if len(args) > 0:  # If at least one additional argument has been passed.

        if args[0] == 'ingest':
            ingest(datasets)

        elif args[0] == 'clean':
            clean(datasets)

        elif args[0] == 'query':

            # If a 2nd arugment has been passed. Expected alias or structure value.
            if len(args) == 2:
                print(f'Top 10 results for: {args[1]}.')
                query(args[1])

            # If a 3rd argument has been passed. Expected quantity.
            if len(args) == 3:

                if args[2].isnumeric():
                    if int(args[2]) < 1001:
                        print(f'Top {args[2]} results for: {args[1]}.')
                        query(args[1], args[2])  # Query, quantity.
                    else:
                        print(f'Top 1,000 results for: {args[1]}.')
                        query(args[1], 1000)  # Query, quantity.
                else:
                    print(
                        f'{args[2]} is not a numeric value, defaulting to top 10 results for: {args[1]}.')
                    query(args[1])

        else:
            print('Invalid argument passed, see README.')
