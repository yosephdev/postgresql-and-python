import psycopg2

# Connect to the database
connection = psycopg2.connect(database="chinook")
cursor = connection.cursor()

# Define the queries
queries = [
    # Query 1 - select all records from the "artist" table
    "SELECT * FROM artist",

    # Query 2 - select only the "Name" column from the "artist" table
    "SELECT name FROM artist",

    # Query 3 - select only "Queen" from the "artist" table
    ("SELECT * FROM artist WHERE name = %(name)s", {"name": "Queen"}),

    # Query 4 - select only by "artist_id" #51 from the "artist" table
    ("SELECT * FROM artist WHERE artist_id = %(artist_id)s", {"artist_id": 51}),

    # Query 5 - select only the albums with "artist_id" #51 on the "album" table
    ("SELECT * FROM album WHERE artist_id = %(artist_id)s", {"artist_id": 51}),

    # Query 6 - select all tracks where the composer is "Queen" from the "track" table
    ("SELECT * FROM track WHERE composer = %(composer)s", {"composer": "Queen"})
]

# Execute the queries and fetch the results
for query in queries:
    if isinstance(query, str):
        cursor.execute(query)
    else:
        cursor.execute(query[0], query[1])
    results = cursor.fetchall()
    for result in results:
        print(result)

# Close the connection
connection.close()
