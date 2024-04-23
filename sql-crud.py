from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql.elements import quoted_name

# Create the database engine
db = create_engine("postgresql:///chinook")

# Create the base class for the ORM models
Base = declarative_base()


class Programmer(Base):
    __tablename__ = quoted_name("Programmer", quote=True)
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


Session = sessionmaker(db)
session = Session()

# Create the database tables
Base.metadata.create_all(db)

# Add new programmer record for myself
myself = Programmer(
    first_name="Yoseph Berhane",
    last_name="Gebremedhin",
    gender="Male",
    nationality="Swedish",
    famous_for="yoseph.dev",
)

# Uncomment the following lines to add the previous records
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="Female",
#     nationality="British",
#     famous_for="First Programmer"
# )
#
# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="Male",
#     nationality="British",
#     famous_for="Modern Computing"
# )
#
# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="Female",
#     nationality="American",
#     famous_for="COBOL language"
# )
#
# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="Female",
#     nationality="American",
#     famous_for="Apollo 11"
# )
#
# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="Male",
#     nationality="American",
#     famous_for="Microsoft"
# )
#
# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="Male",
#     nationality="British",
#     famous_for="World Wide Web"
# )

# Add the new programmer record to the session and commit the changes
# session.add(myself)
session.commit()

# Updating a single record
programmer = session.query(Programmer).filter_by(id=7).first()
programmer.famous_for = "World President"
session.commit()

# Updating multiple records
people = session.query(Programmer)
for person in people:
    if person.gender == "Female" or person.gender == "Male":
        continue
    elif person.gender == "F":
        person.gender = "Female"
    elif person.gender == "M":
        person.gender = "Male"
    else:
        print(f"Gender not defined for {person.first_name} {person.last_name}")
session.commit()

# Deleting a single record
fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer = (
    session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
)
if programmer is not None:
    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted")
    else:
        print("Programmer not deleted")
else:
    print("No records found")

# Deleting multiple/all records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

# Query the Programmer table and print the results
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | ",
    )

# Close the session
session.close()
