import csv

class Contact:
    def __init__(self, name, lastname, phone, email):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email

def createContact(file_path):
    contact_objects = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            name, lastname, phone, email = row
            contact = Contact(name, lastname, phone, email)
            contact_objects.append(contact)
    return contact_objects

file_path = 'contacts.csv'
contacts = createContact(file_path)

def show_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact.name}")
        print(f"Lastname: {contact.lastname}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print()

show_contacts(contacts)