#!/usr/bin/python3

import psycopg2

# SQL code for Preset Reports
# 1. Most viewed articles.
#	 Returns the top 3 viewed articles in descending order. [Article - Views]
mostViewedArticlesReport = "select title, count(*) as views from log join \
articles on log.path like concat('%', articles.slug, '%') group by title \
order by views DESC limit 3;"
# 2. Most Viewed Author.
# 	Returns the views per author in descending order. [Author - Views]
mostViewedAuthorReport = "select name, totalViews.views from authors left \
join (select articles.author, count(*) as views from log  join articles \
on log.path like concat('%', articles.slug, '%')  group by \
articles.author) as totalViews on authors.id = totalViews.author \
order by totalViews.views DESC;"
# 3. HTTP Error Report. Returns the date and rate of page request errors
# Where the error rate is over 1%. [Date - Error Rate]
requestErrorReport = "select date, errorRate from (select cast(time as date) \
as date, (count(case when status = '404 NOT FOUND' then 1 end) * 100 / \
count(status)) as errorRate from log group by date) as errorReport where \
errorRate > 1;"

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
		print('%-40s%-10s' % ("{0}".format(dataReturn[index][0]), "{0}".format(dataReturn[index][1])))
		index += 1
	print('\n\n')


# Display menu tree for User. Initialize the selection, the ask users for
# options 1 through 4.
selection = 0
while selection != 4:
	try:
		print("Select a report.\n1. Most Viewed Articles\n2. Most Viewed Authors\
			\n3. HTTP Request Errors Report\n\nPress '4' to exit")
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
		# Any other input besides our 4 choices are invalid. Return to top of loop.
		else:
			print("Invalid Input.")
			continue
	except:
		print("Invalid Input")
		continue
		