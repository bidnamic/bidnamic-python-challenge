import os

datasets = []  # Initialise empty dataset list.


class Dataset:
    '''
    Builds class object for each dataset.
    Contains attribute for each key found in dataset dictionaries.
    '''

    def __init__(self, dataset):
        dict_values = list(dataset.values())
        self.name = dict_values[0]
        self.fields = dict_values[1]
        self.path = dict_values[2]
        self.create_table = dict_values[3]


adgroups = Dataset(
    {
        'name': 'adgroups',
        'fields': 'ad_group_id, campaign_id, alias,status',
        'path': os.path.abspath('data/adgroups.csv'),
        'create_table': '''
                        CREATE TABLE adgroups(
                        id SERIAL NOT NULL,
                        ad_group_id BIGINT NOT NULL,
                        campaign_id BIGINT NOT NULL,
                        alias VARCHAR(999) NOT NULL,
                        status char(20) NOT NULL,
                        PRIMARY KEY (id))
                        ''',
    }
)

campaigns = Dataset(
    {
        'name': 'campaigns',
        'fields': 'campaign_id, structure_value, status',
        'path': os.path.abspath('data/campaigns.csv'),
        'create_table': '''
                        CREATE TABLE campaigns(
                        id SERIAL NOT NULL,
                        campaign_id BIGINT NOT NULL,
                        structure_value VARCHAR(999) NOT NULL,
                        status CHAR(20) NOT NULL,
                        PRIMARY KEY (id))
                        ''',
    }
)

search_terms = Dataset(
    {
        'name': 'search_terms',
        'fields': 'date, ad_group_id, campaign_id, clicks, cost, conversion_value, conversions, search_term',
        'path': os.path.abspath('data/search_terms.csv'),
        'create_table': '''
                        CREATE TABLE search_terms(
                        id SERIAL NOT NULL,
                        date CHAR(10) NOT NULL,
                        ad_group_id BIGINT NOT NULL,
                        campaign_id BIGINT NOT NULL,
                        clicks INTEGER NOT NULL,
                        cost DECIMAL NOT NULL,
                        conversion_value DECIMAL NOT NULL,
                        conversions INTEGER NOT NULL,
                        search_term varchar(999) NOT NULL,
                        PRIMARY KEY (id))
                        ''',
    }
)

# Append datasets into list for iteration at a later point.
for dataset in adgroups, campaigns, search_terms:
    datasets.append(dataset)
