import psycopg2

conn = psycopg2.connect(database='n48', user='postgres', password='1234', host='localhost', port=5432)

my_cursor = conn.cursor()

select_query = """
select * from category;
"""
my_cursor.execute(select_query)
rows = my_cursor.fetchall()

for row in rows:
    print(row)

"""Successfully added!!!"""
