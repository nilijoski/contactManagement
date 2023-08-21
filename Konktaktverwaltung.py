import csv
import os

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
    print("(Press ENTER to exit to main menu)")
    name = input("Enter the name of the contact to delete: ")
    if(name == ''):
        return
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

def add_contact(contacts):
    print("(Press ENTER to exit to main menu)")
    name = input(f"Please enter the name: ")
    if(name == ''):
        return
    lastname = input(f"Please enter the lastname: ")
    phone = input(f"Please enter the phone number: ")
    email = input(f"Please enter the email address: ")
    
    new_contact = Contact(name, lastname, phone, email)
    contacts.append(new_contact)
    print(f"\nContact '{name} {lastname}' has been added.")
    saveContacts(contacts)

def edit_contact(contacts):
    name_to_edit = input("Enter the name of the contact to edit: ")
    if(name_to_edit == ''):
        return
    lastname_to_edit = input("Enter the lastname of the contact to edit: ")

    for contact in contacts:
        if contact.name == name_to_edit and contact.lastname == lastname_to_edit:
            new_name = input("Enter the new name: ")
            new_lastname = input("Enter the new lastname: ")
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email address: ")

            contact.name = new_name
            contact.lastname = new_lastname
            contact.phone = new_phone
            contact.email = new_email

            saveContacts(contacts)
            print(f"\nContact '{name_to_edit} {lastname_to_edit}' has been updated.")
            return

    print(f"\nContact '{name_to_edit} {lastname_to_edit}' not found.")


def on_start():
    contacts = createContact(file_path)
    while True:
        print("\nWelcome to Contacts Menu\n\nPlease choose one of the following actions by pressing the corresponded number:")
        print("1. Show all contacts")
        print("2. Delete contact")
        print("3. Add contact")
        print("4. Edit contact")
        action = input("Please choose: ")
        if action == '1':
            show_contacts(contacts)
        elif action == '2':
            remove_contact(contacts)
        elif action == '3':
            add_contact(contacts)
        elif action == '4':
            edit_contact(contacts)

on_start()