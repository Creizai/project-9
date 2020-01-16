# Import peewee
from peewee import *
from datetime import date

# Create database connection and connect to 'people' table

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):
        class Meta:
            database = db

# Defining our Person model
class Contact(BaseModel):
    name = CharField()
    phone = IntegerField()
    address = CharField()
    birthday = DateField()
    description = CharField()

# Connect to the PSQL database:
db.connect()
# Drop existing tables (if they exist):
db.drop_tables([Contact])
# Create tables
db.create_tables([Contact])

def create_contact():
    print("Enter the Contact's Name: ")
    new_name = str(input())
    print("Enter the Contact's Phone Number: ")
    new_phone = int(input())
    print("Enter the Contact's Address: ")
    new_address = str(input())
    print("Enter the Contact's Birthday: 2020, 1, 1")
    new_birthday = date(input())
    print("Enter the Contact's description: ")
    new_description = str(input())

    new_contact = Contact(name={new_name}, phone={new_phone}, address={new_address}, birthday=date({new_birthday}), description={new_description})
    new_contact.save()

# zakk = Contact(name="Zakk", phone=2025171777, address="509 7th St NW, Washington, DC 20004", birthday=date(1990, 11, 18), description="The Head SEI34 Instructor")
# erin = Contact(name="Erin", phone=2025171777, address="509 7th St NW, Washington, DC 20004", birthday=date(1986, 1, 27), description="The Head SEI34 Instructor")
# roger = Contact(name="Roger", phone=2025171777, address="509 7th St NW, Washington, DC 20004", birthday=date(1990, 5, 27), description="The Head SEI34 Instructor")
# zakk.save()
# erin.save()
# roger.save()

# Read: (.get() and .select())
def get_contact(name):
    contact = Contact.get(Contact.name == {name})
    print(f'Read {name}:', {contact.name})

# saves each person element with birthday  before 1990, 6, 1 to people 
# contacts = Contact.select().where(Contact.birthday < date(1990, 6, 1))

# for loop that prints for each person in people 
for contact in contacts:
        print(contact.name)
# Person.select()

# Update:
# zakk = Contact.get(Contact.name == 'Zakk')
# zakk.birthday = date(1980, 11, 18)
# zakk.save()

# Delete:
# zakk.delete_instance()


# print(f"{zakk.name} was born on {zakk.birthday}")
# print(f"{erin.name} was born on {erin.birthday}")
# print(f"{roger.name} was born on {roger.birthday}")
