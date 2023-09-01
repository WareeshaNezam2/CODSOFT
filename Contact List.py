print("CONTACT LIST")
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"{name} added to contacts.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
                print("-" * 20)

    def search_contact(self, query):
        results = []
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details['Phone']:
                results.append((name, details))
        if not results:
            print("No matching contacts found.")
        else:
            print("\nSearch Results:")
            for name, details in results:
                print(f"Name: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
                print("-" * 20)

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            print(f"{name}'s contact details updated.")
        else:
            print(f"{name} not found in contacts.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name}'s contact deleted.")
        else:
            print(f"{name} not found in contacts.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_manager.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            query = input("Enter Name or Phone to search: ")
            contact_manager.search_contact(query)
        elif choice == "4":
            name = input("Enter Name to update: ")
            phone = input("Enter new Phone: ")
            email = input("Enter new Email: ")
            address = input("Enter new Address: ")
            contact_manager.update_contact(name, phone, email, address)
        elif choice == "5":
            name = input("Enter Name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "6":
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

