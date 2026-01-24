# Contact Book Application

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    search = input("Enter name or phone to search: ")

    found = False
    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print("\n Contact Found:")
            print(contact)
            found = True

    if not found:
        print("Contact not found.\n")


def update_contact():
    phone = input("Enter phone number of contact to update: ")

    for contact in contacts:
        if contact['phone'] == phone:
            print("Enter new details:")
            contact['name'] = input("New Name: ")
            contact['email'] = input("New Email: ")
            contact['address'] = input("New Address: ")
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


def delete_contact():
    phone = input("Enter phone number to delete contact: ")

    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


def main():
    while True:
        print("===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()
