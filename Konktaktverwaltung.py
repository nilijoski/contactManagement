import csv


file_path = 'contacts.csv'
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
    
def saveContacts(contacts):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for contact in contacts:
            csv_writer.writerow([contact.name, contact.lastname, contact.phone, contact.email])


def show_contacts(contacts):
    print()
    count = 0
    for contact in contacts:
        count += 1
        print(f"{count} {contact.name} {contact.lastname} {contact.phone} {contact.email}")

def remove_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    lastname = input("Enter the lastname of the contact to delete: ")
    deleted = False
    for contact in contacts:
        if contact.name == name and contact.lastname == lastname:
            contacts.remove(contact)
            deleted = True
            break
    if(deleted):
        print(f"\nContact '{name} {lastname}' has been deleted.")
        saveContacts(contacts)
        
    else:
        print(f"\nContact '{name} {lastname}' not found.")

        
def on_start():
    contacts = createContact(file_path)
    while True:
        print("\nWelcome to Contacts Menu\n\nPlease choose one of the following actions by pressing the corresponded number:")
        print("1. Show all contacts")
        print("2. Delete contact")
        print("3. Edit contact")
        action = input("Please choose: ")
        if (action == '1'):
            show_contacts(contacts)
        elif (action == '2'):
            remove_contact(contacts)
        elif(action == '3'):
            print("in work...")



on_start()