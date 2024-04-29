class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

def add_contact(contacts):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(name, phone_number, email, address)
    contacts.append(contact)
    print("Contact added successfully!")

def view_contact_list(contacts):
    print("Contact List:")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. Name: {contact.name}, Phone: {contact.phone_number}")

def search_contact(contacts, query):
    results = []
    for contact in contacts:
        if query.lower() in contact.name.lower() or query in contact.phone_number:
            results.append(contact)
    return results


def main():
    contacts = []
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contact_list(contacts)
        elif choice == "3":
            query = input("Enter search query: ")
            results = search_contact(contacts, query)
            if results:
                print("Search results:")
                for contact in results:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
