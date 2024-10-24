import os

CONTACTS_FILE = 'contacts.txt'

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as file:
        return [line.strip().split('|') for line in file]

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        for contact in contacts:
            file.write('|'.join(contact) + '\n')

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append([name, phone, email])
    save_contacts(contacts)
    print("Contact added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]} | {contact[1]} | {contact[2]}")

def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Invalid selection.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
