# Full Stack Web Developer Nanodegree Project: Logs Analysis

This project was completed as part of the Udacity Full Stack Web Developer Nanodegree.

The task is to create a reporting tool that prints out reports (in plain text) based on the data in a PostgreSQL database. 
This reporting tool is a Python program using the psycopg2 module to connect to the database.

[Project rubric](https://review.udacity.com/#!/rubrics/277/view)

## Program name
  logs-analysis.py

## Project Dependencies

1. [Full Stack Nanodegree virtual machine](https://github.com/jbaldwin01/fullstack-nanodegree-vm)
2. PostgreSQL database
3. [news](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) data
4. Database view log_requests:
```sql
CREATE VIEW log_requests AS
SELECT DATE(log."time") AS date,
    COUNT(log."time") AS requests
   FROM log
  GROUP BY (DATE(log."time"))
  ORDER BY (DATE(log."time"));
```

5. Database view error_stats:
```sql
CREATE VIEW error_stats AS
SELECT DATE(time) AS date, COUNT(time) AS errors, requests, COUNT(time)/CAST(requests AS FLOAT)*100 AS error_percentage
FROM log JOIN log_requests ON DATE(time) = log_requests.date
WHERE status != '200 OK' -- errors
GROUP BY DATE(time), requests
ORDER BY DATE(time);
```

## Running the program

```python logs-analysis.py```
