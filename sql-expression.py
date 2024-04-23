from sqlalchemy import create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData

# Create the engine
engine = create_engine("postgresql:///chinook")

# Create the metadata object
metadata = MetaData()

# Define the tables
artist_table = Table(
    "artist", metadata,
    Column("artist_id", Integer, primary_key=True),
    Column("name", String)
)

album_table = Table(
    "album", metadata,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist.artist_id"))
)

track_table = Table(
    "track", metadata,
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album.album_id")),
    Column("media_type_id", Integer),
    Column("genre_id", Integer),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float)
)

# Bind the engine to the metadata
metadata.bind = engine

# Connect to the database and perform operations
with engine.connect() as connection:
    # Query 1 - select all records from the "artist" table
    select_query = artist_table.select()
    results = connection.execute(select_query)
    for result in results:
        print(result)

    # Query 2 - select only the "name" column from the "artist" table
    select_query = artist_table.select().with_only_columns(artist_table.c.name)
    results = connection.execute(select_query)
    for result in results:
        print(result)

    # Query 3 - select only 'Queen' from the "artist" table
    select_query = artist_table.select().where(artist_table.c.name == "Queen")
    results = connection.execute(select_query)
    for result in results:
        print(result)

    # Query 4 - select only by 'artist_id' #51 from the "artist" table
    select_query = artist_table.select().where(artist_table.c.artist_id == 51)
    results = connection.execute(select_query)
    for result in results:
        print(result)

    # Query 5 - select only the albums with 'artist_id' #51 on the "album" table
    select_query = album_table.select().where(album_table.c.artist_id == 51)
    results = connection.execute(select_query)
    for result in results:
        print(result)

    # Query 6 - select all tracks where the composer is 'Queen' from the "track" table
    select_query = track_table.select().where(track_table.c.composer == "Queen")
    results = connection.execute(select_query)
    for result in results:
        print(result)
