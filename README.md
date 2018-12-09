# UD-LogsAnalysis

This program can create 3 reports from existing database data. The user will be prompted to select one of the reports.
1. Display the 3 most viewed articles and the number of times they have been viewed.
2. Display all of the authors and their total number of views.
3. Display an HTTP Error Report that shows any days with a status failure rate of 1% or more. 

The program assumes you have a database named 'news' already populated and in the same location as this program.

The SQL query strings are coded only for these 3 reports and can only be selected by integer selection from the user prompt. Any other input should be caught and returned to root menu. 

Press '4' to exit program. 
