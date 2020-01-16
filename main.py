# Import peewee
from peewee import *
from datetime import date

# Create database connection and connect to 'people' table

db = PostgresqlDatabase('contacts_book', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):
        class Meta:
            database = db

# Defining our Person model
class Contact(BaseModel):
    name = CharField()
    phone = CharField()
    address = CharField()
    description = CharField()

# Connect to the PSQL database:
db.connect()


# Drop existing tables (if they exist):
# db.drop_tables([Contact])

# Create tables
db.create_tables([Contact])


def create_contact():
    new_name = input("Enter the Contact's Name: ")
    new_phone = input("Enter the Contact's Phone Number: ")
    new_address = input("Enter the Contact's Address: ")
    new_description = input("Enter the Contact's description: ")

    new_contact = Contact(name=new_name, phone=new_phone, address=new_address, description=new_description)
    new_contact.save()

# adam = Contact(
#     name="Adam", 
#     phone=(5134179949), 
#     address="4802 Chief Chris Kyle Ct", 
#     description="Loud and annoying")
# adam.save()
# erin = Contact(name="Erin", phone=2025171777, address="509 7th St NW, Washington, DC 20004", birthday=date(1986, 1, 27), description="The Head SEI34 Instructor")
# roger = Contact(name="Roger", phone=2025171777, address="509 7th St NW, Washington, DC 20004", birthday=date(1990, 5, 27), description="The Head SEI34 Instructor")
# zakk.save()
# erin.save()
# roger.save()

# Read: (.get() and .select())
def get_contact(name):
    contact = Contact.get(Contact.name == name)
    print(f'Read name: {contact.name} Phone Number: {contact.phone} Address: {contact.address} Description: {contact.description}')

def all_contacts():
    contacts = Contact.select()
    # print(f'Read name: {contact.name} Phone Number: {contact.phone} Address: {contact.address} Description: {contact.description}')
    # Contact.select()
    print('--CONTACTS BOOK--')
    for contact in contacts:
        print('-----------------\n')
        print(contact.name)
        print(contact.phone)
        print(contact.address)
        print(contact.description)
        print('\n-----------------')
    


# saves each person element with birthday  before 1990, 6, 1 to people 
# contacts = Contact.select().where(Contact.birthday < date(1990, 6, 1))

# for loop that prints for each person in people 
# for contact in contacts:
#         print(contact.name)
# Person.select()

# Update:
# zakk = Contact.get(Contact.name == 'Zakk')
# zakk.birthday = date(1980, 11, 18)
# zakk.save()
def update_contact():
    name = str(input("Enter the name of the contact you want to Update: "))
    contact = Contact.get(Contact.name == name)
    update = 0
    while update != 5:
        print('\nWhat Key would you like to update?\n')
        print('1. Name')
        print('2. Phone Number')
        print('3. Address')
        print('4. Description')
        print('5. None! Get me outta here!)
        update = int(input('Enter #:'))
        if(update == 1):
            print(f'Old Name: ' {contact.name})
            contact.name = input("Enter New Name: ")
            contact.save()
            print('Name Changed!')
        elif(update == 2):
            print(f'Old Phone Number: ' {contact.phone})
            contact.phone = input("Enter New Phone Number: ")
            contact.save()
            print('Phone Number Changed!')            
        elif(update == 3):
            print(f'Old Address: ' {contact.address})
            contact.address = input("Enter New Address: ")
            contact.save()
            print('Address Changed!')            
        elif(update == 4):
            print(f'Old Description: ' {contact.description})
            contact.description = input("Enter New Description: ")
            contact.save()
            print('Description Changed!')            

# Delete:
# zakk.delete_instance()
def delete_contact():
    name = str(input("Enter the name of the contact you want to Delete: "))
    contact = Contact.get(Contact.name == name)
    contact.delete_instance()
    print("\n Deleted Contact!\n")


# print(f"{zakk.name} was born on {zakk.birthday}")
# print(f"{erin.name} was born on {erin.birthday}")
# print(f"{roger.name} was born on {roger.birthday}")

navigation = 0
while navigation != 5:
    print('\nContacts Book\n')
    print('1. Create a new contact')
    print('2. Read all contacts')
    print('3. Update a contact')
    print('4. Delete a contact')
    print('5. Exit the Program')
    navigation = int(input('Enter #:'))
    if(navigation == 1):
        create_contact()
    elif(navigation == 2):
        all_contacts()
    elif(navigation == 3):
        update_contact()
    elif(navigation == 4):
        delete_contact()
