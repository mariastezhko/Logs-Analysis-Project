#!/usr/bin/python3
#
# Logs Analysis Project
#

import psycopg2

DBNAME = "news"

# A function that connects to a database,
# executes a query, and returns a result


def get_query_result(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        return c.fetchall()
        db.close
    except Exception as e:
        print(e)
        exit(1)


# A function that formats and prints the result of a query


def print_query_result(result, last_word):
    for i in range(len(result)):
        str1 = result[i][0]
        str2 = result[i][1]
        print("     {} --- {}{}".format(str1, str2, last_word))


#
# Queries
#

# The most popular three articles of all time
query_articles = (
    "select articles.title, count(*) as num "
    "from log, articles "
    "where log.path = concat('/article/', articles.slug) "
    "and log.status like '%200%' "
    "group by articles.title, log.path "
    "order by num desc "
    "limit 3;")
query_articles_title = ("The most popular three articles of all time\n")

# The most popular article authors of all time
query_authors = (
    "select authors.name, count(*) as num "
    "from log, articles, authors "
    "where (articles.author = authors.id) and "
    "log.path = concat('/article/', articles.slug) "
    "and log.status like '%200%' "
    "group by authors.name "
    "order by num desc;")
query_authors_title = ("The most popular article authors of all time\n")

# The days on which more than 1% of requests led to errors
query_errors = (
    "select to_char(date1, 'Mon DD, YYYY') as day, "
    "round((100.0*num2)/num1, 2) as error_percent "
    "from ("
    # Subquery that retrieves total requests on each day
    "(select date(TIME) as date1, count(*) as num1 from log "
    "group by date1 order by num1 desc) as total_requests "
    "join "
    # Subquery that retrieves error requests on each day
    "(select date(TIME) as date2, count(*) as num2 from log "
    "where status not like '%200 OK%' "
    "group by date2 order by num2 desc) as error_requests "
    "on "
    "total_requests.date1 = error_requests.date2 "
    ") as stats "
    "where round((100.0*num2)/num1, 1) > 1.0 "
    "order by error_percent desc;")
query_error_title = (
    "The days on which more than 1% of requests led to errors\n")

popular_articles = get_query_result(query_articles)
popular_authors = get_query_result(query_authors)
error_requests = get_query_result(query_errors)

print("")
print(query_articles_title)
print_query_result(popular_articles, " views")
print("")
print(query_authors_title)
print_query_result(popular_authors, " views")
print("")
print(query_error_title)
print_query_result(error_requests, "% errors")
