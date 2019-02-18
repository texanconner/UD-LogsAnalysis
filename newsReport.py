#!/usr/bin/python3

import psycopg2

# SQL code for Preset Reports
# 1. Most viewed articles.
# Returns the top 3 viewed articles in descending order. [Article - Views]

mostViewedArticlesReport = """SELECT title, count(*) AS views
    FROM log join articles ON log.path
    LIKE concat('%', articles.slug, '%')
    AND log.status='200 OK'
    GROUP BY title
    ORDER BY views DESC limit 3;"""


# 2. Most Viewed Author.
# 	Returns the views per author in descending order. [Author - Views]

mostViewedAuthorReport = """SELECT name, totalViews.views
    FROM authors LEFT JOIN (
        SELECT articles.author, count(*) AS views
        FROM log join articles ON log.path
        LIKE concat('%', articles.slug, '%')
        AND log.status='200 OK'
        GROUP BY articles.author) AS totalViews
    ON authors.id = totalViews.author
    ORDER BY totalViews.views DESC;"""


# 3. HTTP Error Report. Returns the date and rate of page request errors
# Where the error rate is over 1%. [Date - Error Rate]

requestErrorReport = """SELECT date, errorRate
    FROM (
        SELECT cast(time AS date) AS date,
        (count(case when status = '404 NOT FOUND' then 1 end) * 100
            / count(status))
        AS errorRate
        FROM log
        GROUP BY date) AS errorReport
    WHERE errorRate > 1;"""

# Function takes in a string of sql commands, connects to a database,
# Runs the sql commands and returns the result.
# Input is valid SQL code
# Returns a database table


def reporter(report):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(report)
    query = c.fetchall()
    db.close()
    return query


# Function prints the request data
# Input is a table/list returned by the reporter function.
# Expected output is printing the data into columns on the screen with header.


def printData(reportData):
    index = 0
    for reportDatas in reportData:
        print('%-40s%-10s' % ("{0}".format(dataReturn[index][0]), "{0}\
        ".format(dataReturn[index][1])))
        index += 1
    print('\n\n')


# Display menu tree for User. Initialize the selection, the ask users for
# options 1 through 4.
selection = 0
while selection != 4:
    try:
        print("Select a report.\n1. Most Viewed Articles\n2. Most Viewed\
 Authors\n3. HTTP Request Errors Report\n\nPress '4' to exit")
        selection = input("-->")
        # Article Report
        if selection == 1:
            print("Running Report... Please wait.\n")
            dataReturn = reporter(mostViewedArticlesReport)
            print('%-40s%-10s' % ("Article", "Views"))
            printData(dataReturn)
            continue
        # Author Report
        if selection == 2:
            print("Running Report... Please wait.\n")
            dataReturn = reporter(mostViewedAuthorReport)
            print('%-40s%-10s' % ("Author", "Views"))
            printData(dataReturn)
            continue
        # HTTP Error Report
        if selection == 3:
            print("Running Report... Please wait.\n")
            dataReturn = reporter(requestErrorReport)
            print('%-40s%-10s' % ("Date", "Error Rate (%)"))
            printData(dataReturn)
            continue
        # Exit Program
        if selection == 4:
            exit()
        # Any other input besides our 4 choices are invalid.
        # Return to top of loop.
        else:
            print("Invalid Input.")
            continue
    except:  # noqa: E722
        print("Goodbye")
        continue
