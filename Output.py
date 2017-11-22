import NewsDB

# storing the returned results from the queries
top_authors_set = NewsDB.get_top_authors()
top_articles_set = NewsDB.get_top_articles()
top_error_set = NewsDB.get_error()

# Returning the most popular articles of all time
print('****** What are the most popular three articles of all time? ******')

i = 0
for top_articles in top_articles_set:
    i = i + 1
    top_articles_name = top_articles[0]
    top_articles_count = str(top_articles[1])
    print(str(i) + ". '" + top_articles_name + "'" + " ---- " + top_articles_count + " views")

# Returning the most popular authors of all time
print('******Who are the most popular authors of all time?******')

i = 0
for top_authors in top_authors_set:
    i = i + 1
    top_authors_name = top_authors[0]
    top_authors_count = str(top_authors[1])
    print(str(i) + ". '" + top_authors_name + "'" + " ---- " + top_authors_count + " views")

# Returning the day where the 404 error % is the highest
i = 0
print('******On which days did more than 1% of requests lead to errors?******')
for top_error in top_error_set:
    i = i + 1
    top_error_day = str(top_error[0])
    top_error_ratio = str(top_error[1])
    print(str(i) + ". '" + top_error_day + "'" + " has an error ratio of " + top_error_ratio + "%")
