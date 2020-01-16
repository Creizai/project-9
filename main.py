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

#Create new Contact
def create_contact():
    new_name = input("Enter the Contact's Name: ")
    new_phone = input("Enter the Contact's Phone Number: ")
    new_address = input("Enter the Contact's Address: ")
    new_description = input("Enter the Contact's description: ")
    #Create new Contact Instance with users data
    new_contact = Contact(name=new_name, phone=new_phone, address=new_address, description=new_description)
    new_contact.save()

# Read: (.get() and .select())
def get_contact(name):
    contact = Contact.get(Contact.name == name)
    print(f'Read name: {contact.name} Phone Number: {contact.phone} Address: {contact.address} Description: {contact.description}')

# Use Select all contacts and a For Loop iterate through all contacts to print them
def all_contacts():
    contacts = Contact.select()
    print('--CONTACTS BOOK--')
    for contact in contacts:
        print('-----------------\n')
        print(f'Contact {contact.name}')
        print(f'Phone Number: {contact.phone}')
        print(f'Address: {contact.address}')
        print(f'Description: {contact.description}')
        print('\n-----------------')

def update_contact():
    name = str(input("\nEnter the name of the contact you want to Update: "))
    contact = Contact.get(Contact.name == name)
    get_contact(name)
    update = 0
    while update != 5:
        print('\nWhat Key would you like to update?\n')
        print('1. Name')
        print('2. Phone Number')
        print('3. Address')
        print('4. Description')
        print('5. None! Get me outta here!')
        update = int(input('Enter #:'))
        if(update == 1):
            print(f'Old Name: {contact.name}')
            contact.name = input("Enter New Name: ")
            contact.save()
            print('Name Changed!')
        elif(update == 2):
            print(f'Old Phone Number: {contact.phone}')
            contact.phone = input("Enter New Phone Number: ")
            contact.save()
            print('Phone Number Changed!')            
        elif(update == 3):
            print(f'Old Address: {contact.address}')
            contact.address = input("Enter New Address: ")
            contact.save()
            print('Address Changed!')            
        elif(update == 4):
            print(f'Old Description: {contact.description}')
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
