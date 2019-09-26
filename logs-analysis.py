#!/usr/bin/env python3

import psycopg2
import sys

DBNAME = "news"

try:
    dbconn = psycopg2.connect(database=DBNAME)
except psycopg2.Error as e:
    print("Unable to connect to the database")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)
c = dbconn.cursor()
query1 = """select title, count(path) as views
from articles
join log on articles.slug = substring(log.path from 10)
where status = '200 OK'
and length(path) > 1
group by title
order by views desc
limit 3;"""

query2 = """select name, count(path) as views
from authors
join articles on authors.id = articles.author
join log on articles.slug = substring(log.path from 10)
where status = '200 OK'
and length(path) > 1
group by name
order by views desc;"""

query3 = """select date, round(cast(error_percentage as numeric), 1)
as percent_errors
from error_stats
where error_percentage > 1;"""

# Solution 1
c.execute(query1)
rows = c.fetchall()

print("Question one solution:")
for row in rows:
    print("'" + row[0] + "'" + " - " + str(row[1]) + " views")

# Solution 2
c.execute(query2)
rows = c.fetchall()

print("\nQuestion two solution:")
for row in rows:
    print(row[0] + " - " + str(row[1]) + " views")

# Solution 3
c.execute(query3)
rows = c.fetchall()

print("\nQuestion three solution:")
for row in rows:
    print(str(row[0]) + " - " + str(row[1]) + "% errors")

dbconn.close()
