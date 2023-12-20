import database
# Add a record to the database
database.add_one("James", "Paul", "james@2paul.com")
# Drop Record
database.delete_one('1')

# Lookup first name
database.name_lookup("Pompey")


stuff = [
    ("Pompey","Rome","pom@rome.com"),
    ("Gladiator","Rome","gald@rome.com")
]

database.add_many(stuff)

# Querry all database
database.show_all()



