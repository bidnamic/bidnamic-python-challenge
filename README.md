# **Jamie Bowman's Bidnamic challenge submission**

## **Getting started**

### **Requirements**

This submission requires a local installation of PostgreSQL.
Within PostgreSQL, a standard user will need to be created, along with an empty database that the user has read/write permissions for.
Additionally, this submission requires python with a version of at least v3.6 (Aug 2016), which allows use f-strings. 

### **Clone this repository**

Download this repository via the code drop down menu (top right), by selecting 'Download ZIP'. Extract from zip once downloaded.

### **Create virtual environment & import packages**

Use 'requirements.txt' file to create a virtual environment.
This can be done by opening a terminal at the root directory for the newly cloned directory, and entering the following command:

**python -m venv .venv**

To enable the newly created virtual environment, in the same terminal, enter the following:

*(Windows)* > **.venv\Scripts\activate.bat**

*(Linux & Mac)* > **source .venv/bin/activate**

To confirm that the virtual environment is now active, check for **(.venv)** at the start of the terminal's prompt.
To import the required packages, in the activated virtual environment, enter the following:

**python -m pip install -r requirements.txt**

### **Update database.ini**

To allow this submission to connect to your locally installed PostgreSQL database, the **example_database.ini** file needs to be updated with the correct credentials.
Make a copy of the **example_database.ini**, and rename it as **database.ini**.
Open the newly copied **database.ini** with any text editor, and update the following:

**<enter_db_name>**: to the name of the newly created database within PostgreSQL.

**<enter_db_username>**: to the username created for this submission. (Requires read/write access to above database.)

**<enter_db_password>**: to the password for the above user.

(If your instance of PostgreSQL uses a custom port, the port will also need to be updated to match, if this has not been changed in your setup, the default value is fine.)

### **Placing dataset files**

The supplied dataset files will need to be placed in a dedicated folder. (These could not be uploaded due to file size limitation.)

In the root of the newly cloned and extracted directory, create a new folder named: **data**.

Place the 3 supplied dataset files in this new **data** folder. (Expected: **adgroups.csv**, **campaigns.csv**, **search_terms.csv**)

## **Usecase examples**

*(With the virtual environment activated.)*

### **Ingesting data into database**

This function will do the following for each of the supplied dataset files:
Check to see if a table exists within the dedicated PostgreSQL database.
If they don't exist, it will create them. If they do exist, it will any existing data that's in the table.
Ingest the data from the data file into the empty table.

In a terminal pointed at the root of the cloned directory, enter the following:

**py main.py ingest**

### **Clearing database**

This function will do the following for each of the supplied dataset files:

Check if a table exists.

If it does exists, delete it.

### **Querying database**

This function will query the database for the top *n* search terms for a given query.

It takes one required argument, and one optional argument.
The required argument should be equal to a **structure_value** from the campaigns dataset file, or **alias** from the adgroups dataset file.
The optional argument should be an integer value, equal to the number of desired results.
There are checks in place to ensure that the optional argument is an integer value, and less than 1,000.
(If it's not an integer, or over 1,000, it will be defaulted to 10.)
The query will be used to search for a partial match in the adgroup's alias field, which incedently contains a full string match for campaign's structure value.
This allows the user to search for an exact term from a campaign's structure value, or any partial string from adgroup's alias.

To query the database for the top 10 results for a structure value or alias, *Nike* for example, enter the following into the terminal:

**py main.py query nike**

If you wish to search for a query that has a space in it, encapsulate the query in quotation, as follows:

**py main.py query "north face"**

If you want to change the number of results for a query, follow the query term with an integer value, as follows:

**py main.py query adidas 50**