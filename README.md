# UD-LogsAnalysis

This program can create 3 reports from existing database data.


# Requirements:

* Python (Tested with Python3.7)
* Python Library psycopg2 installed (A PostgreSQL adapter for the Python programming language)
* Vagrant (for a virtual machine)
* PostgreSQL
* Python Module psycopg2 `pip install psycopg2`

# VM and Vagrant Setup
Virtual box can be found and installed from here:
https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

Vagrant can be found and installed from here:
https://www.vagrantup.com/downloads.html

We'll need the vagrant file for this VM configuration.
Clone this repo and inside will be the VM files:
https://github.com/udacity/fullstack-nanodegree-vm

After cloning to your local drive, navigate to the vagrant folder in that repo.

Once in the Vagrant directory, use the `vagrant up` command.
Once the VM is up, next use the `vagrant ssh` command.

The VM should be set up to work with the database now. 

Add the files from this repo to the vagrant folder.

# Database Setup:

The program assumes you have a database named 'news' already populated and in the same location as this program. To create this database, 
The Zip file with database can be downloaded from here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Unzip this in your vagrant directory. From your vagrant directory, run this command to setup the database.
```psql -d news -f newsdata.sql```

The news database should be set up and ready for SQL commands now.

# Running the Program.

In your vagrant session, run the newsReport.py program.
```python newsReport.py```

The user will be prompted to select one of the reports.
1. Display the 3 most viewed articles and the number of times they have been viewed.
2. Display all of the authors and their total number of views.
3. Display an HTTP Error Report that shows any days with a status failure rate of 1% or more. 

The SQL query strings are coded only for these 3 reports and can only be selected by integer selection from the user prompt. Any other input should be caught and returned to root menu. 

Press '4' to exit program. 
