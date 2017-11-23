# importing the library for PostgreSQL operations
import psycopg2

# The name of the database
DBNAME = 'news'


# Cleaning the data and create the keys connecting table articles and log
def org_data():
    # connecting to the database and creating the SQL commands
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Removing the prefix in path
    c.execute("UPDATE log "
              "SET path = REPLACE(path, '/article/', '') "
              "WHERE path LIKE '%/article/%';"
              )
    db.commit()

    # Adding a new column articles_id in log
    c.execute('Alter Table log '
              'ADD articles_id integer;'
              )
    db.commit()

    # Update the value of log.articles_id with articles.id by matching slug
    c.execute('Update log '
              'SET articles_id = (Select articles.id '
              'From articles where articles.slug = log.path);'
              )
    db.commit()
    db.close()

    
def get_top_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Return the no. of views for each article in a descending order
    c.execute('Select articles.title, count(*) '
              'from log '
              'Inner Join articles ON log.articles_id = articles.id '
              'GROUP BY articles.title '
              'ORDER BY count(*) DESC '
              'LIMIT 3;'
              )
    return c.fetchall()
    db.close()


def get_top_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Return the no. of views for each author in a descending order
    c.execute('SELECT authors.name, count(*) '
              'FROM authors '
              'INNER JOIN articles ON authors.id=articles.author '
              'INNER JOIN log on articles.id=log.articles_id '
              'GROUP BY authors.id '
              'ORDER BY count(*) DESC;')
    return c.fetchall()
    db.close()

    
def get_error():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Drop if the views already exist
    c.execute("DROP VIEW IF EXISTS view_error; "
              "DROP VIEW IF EXISTS view_total; "
              )
    db.commit()

    # Create views for no. of error incidences for each day - i.e. 404 error
    c.execute("Create View view_error As "
              "Select date(log.time) as day, count(*) from log "
              "WHERE log.status LIKE '%404%' "
              "Group by date(log.time); "
              )
    db.commit()

    # Create views for total no. of incidences for each day - i.e. both 200 Success and 404 error
    c.execute("Create View view_total As "
              "Select date(log.time) as day, count(*) from log "
              "Group by date(log.time); "
              )
    db.commit()

    # Return the ratio of error as a % of total connections for a particular day
    c.execute("Select view_total.day, 100*view_error.count/view_total.count as error_ratio "
              "from view_total "
              "Left Join view_error ON view_error.day=view_total.day "
              "WHERE 100*view_error.count/view_total.count > 1; "
              )
    return c.fetchall()
    db.close()
