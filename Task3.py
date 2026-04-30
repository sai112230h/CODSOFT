contacts = []   # List to store all contacts

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.\n")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print()

def search_contact():
    search = input("Enter Name or Phone Number to search: ")
    found = False
    for contact in contacts:
        if contact["name"] == search or contact["phone"] == search:
            print("Contact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    search = input("Enter Name of the contact to update: ")
    for contact in contacts:
        if contact["name"] == search:
            print("Enter new details (leave blank to keep old value):")
            new_phone = input("New Phone Number: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")
    
def delete_contact():
    search = input("Enter Name of the contact to delete: ")
    for contact in contacts:
        if contact["name"] == search:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

# Main Menu
def menu():
    while True:
        print("===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

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
            print("Exiting Contact Book... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
menu()
