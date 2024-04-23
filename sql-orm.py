from sqlalchemy import create_engine, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create the database engine
db = create_engine("postgresql:///chinook")

# Create the base class for the ORM models
Base = declarative_base()

# Define the ORM models
class Artist(Base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)

class Album(Base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))

class Track(Base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.album_id"))
    media_type_id = Column(Integer)
    genre_id = Column(Integer)
    composer = Column(String)
    milliseconds = Column(Integer)
    bytes = Column(Integer)
    unit_price = Column(Float)

# Create the session
Session = sessionmaker(db)
session = Session()

# Create the database tables
Base.metadata.create_all(db)

# Define the queries
queries = [
    # Query 1 - select all records from the "artist" table
    (session.query(Artist), "artist"),

    # Query 2 - select only the "name" column from the "artist" table
    (session.query(Artist.name), "artist_name"),

    # Query 3 - select only "Queen" from the "artist" table
    (session.query(Artist).filter_by(name="Queen"), "queen"),

    # Query 4 - select only by "artist_id" #51 from the "artist" table
    (session.query(Artist).filter_by(artist_id=51), "artist_51"),

    # Query 5 - select only the albums with "artist_id" #51 on the "album" table
    (session.query(Album).filter_by(artist_id=51), "albums_51"),

    # Query 6 - select all tracks where the composer is "Queen" from the "track" table
    (session.query(Track).filter_by(composer="Queen"), "queen_tracks")
]

# Execute the queries and fetch the results
for query, name in queries:
    print(f"Query {name}:")
    if name == "artist":
        for artist in query.all():
            print(f"Artist ID: {artist.artist_id}, Name: {artist.name}")
    elif name == "artist_name":
        for name in query.all():
            print(name.name)
    elif name == "queen":
        for artist in query.all():
            print(f"Artist ID: {artist.artist_id}, Name: {artist.name}")
    elif name == "artist_51":
        for artist in query.all():
            print(f"Artist ID: {artist.artist_id}, Name: {artist.name}")
    elif name == "albums_51":
        for album in query.all():
            print(f"Album ID: {album.album_id}, Title: {album.title}, Artist ID: {album.artist_id}")
    elif name == "queen_tracks":
        for track in query.all():
            print(
                f"Track ID: {track.track_id}, Name: {track.name}, Album ID: {track.album_id}, "
                f"Media Type ID: {track.media_type_id}, Genre ID: {track.genre_id}, "
                f"Composer: {track.composer}, Milliseconds: {track.milliseconds}, "
                f"Bytes: {track.bytes}, Unit Price: {track.unit_price}"
            )
    print()

# Close the connection
session.close()