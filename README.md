# Full Stack Web Developer Nanodegree Project: Logs Analysis

This project was completed as part of the Udacity Full Stack Web Developer Nanodegree.

The task is to create a reporting tool that prints out reports (in plain text) based on the data in a PostgreSQL database. 
This reporting tool is a Python program using the psycopg2 module to connect to the database.

[Project rubric](https://review.udacity.com/#!/rubrics/277/view)

## Program name:
  project-logs.py

## Project Dependencies

1 log_requests view:
```sql
create view log_requests as
SELECT date(log."time") AS date,
    count(log."time") AS requests
   FROM log
  GROUP BY (date(log."time"))
  ORDER BY (date(log."time"));
```

2 error_stats view:
```sql
create view log_requests as
SELECT date(log."time") AS date,
    count(log."time") AS requests
   FROM log
  GROUP BY (date(log."time"))
  ORDER BY (date(log."time"));
```

## Running the program

```python logs-analysis.py```
