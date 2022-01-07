<img src="logo.png" alt="drawing" width="500"/>

## Python Software Engineering Challenge

Our system ingests search term data from Google Ads API into a PostgreSQL database, via an AWS S3 Data Lake.

Once ingested we score each search term with its Return On Ad Spend (ROAS).

```text
ROAS = conversion value / cost
```

### Task

1. Some CSVs have been given (campaigns.csv, adgroups.csv and search_terms.csv). Ingest these 3 CSVs into a database.


2. Create some private end points to return the Top 10 Search Terms by ROAS for a campaign `structure_value` or adgroup `alias`.


### Submission

We really value neatness and things being put in place to aid local development and continuous integration.

Please fork this repo to complete the challenge.

Good luck we are rooting for you, show us what you can do!