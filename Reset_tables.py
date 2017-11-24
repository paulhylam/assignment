#!/usr/bin/env python3

# importing the library for PostgreSQL operations
import psycopg2

# The name of the database
DBNAME = 'news'


# Reset all the tables
def reset_data():
    # connecting to the database and creating the SQL commands
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("DROP VIEW IF EXISTS view_error; "
              "DROP VIEW IF EXISTS view_total; "
              "DROP TABLE IF EXISTS log; "
              "DROP TABLE IF EXISTS articles; "
              "DROP TABLE IF EXISTS authors; "
              )
    db.commit()

    # sql_file = open('newsdata.sql', 'r')
    # c.execute(sql_file.read())
    # db.commit()


reset_data()
