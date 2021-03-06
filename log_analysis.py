#!/usr/bin/env python
import psycopg2


# Makes database a vairable so you can switch out to other datasbases
db_name = "news"


query_one = "1.What are the most popular three articles of all time?\n"
query_one_ans = """
                SELECT articles.title, COUNT(*) AS num
                FROM articles JOIN log ON log.path
                LIKE concat('/article/%', articles.slug)
                GROUP BY articles.title
                ORDER BY num DESC
                LIMIT 3;
                """

query_two = "2.Who are the most popular article authors of all time?\n"
query_two_ans = """
                SELECT authors.name, COUNT(*) AS num
                FROM authors
                JOIN articles ON authors.id = articles.author
                JOIN log ON log.path like concat('/article/%', articles.slug) 
                GROUP BY authors.name 
                ORDER BY num DESC 
                LIMIT 4;
                """

query_three = "3.On which days did more than 1% of requests lead to errors?\n"
query_three_ans = """
                  SELECT total.day,
                  ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
                  FROM (
                  SELECT date_trunc('day', time) 'day', count(*) AS error_requests
                  FROM log
                  WHERE status LIKE '404%'
                  GROUP BY day) AS errors
                  JOIN (
                  SELECT date_trunc('day', time) 'day', count(*) AS requests
                  FROM log
                  GROUP BY day) AS total
                  ON total.day = errors.day
                  WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
                  ORDER BY percent DESC;
                  """


# Boilerplate code for query requests with psycopg2
# Takes in the queries declared above this comment to output the solutions
def get_query(query):
    try:
        db = psycopg2.connect(database=db_name)
        c = db.cursor()
        c.execute(query)
        q = c.fetchall()
        db.close()
        for row in q:
            print "'{0}' -- {1} ".format(row[0], row[1])
        print "\n"
     except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Will run if this script is run directly.
# If imported, the get_query function only will be retreived for anyone
# to input their queries and/or databases
if __name__ == '__main__':
    print query_one
    get_query(query_one_ans)

    print query_two
    get_query(query_two_ans)

    print query_three
    get_query(query_three_ans)
