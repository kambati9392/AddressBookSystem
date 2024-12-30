from collections import defaultdict

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state} , {self.zip_code}, {self.phone}, {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = defaultdict(list)

    def add_contact(self, first_name, last_name, address, city, state, zip_code, phone, email):
        new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        self.contacts[first_name].append(new_contact) 

    def del_contacts(self, first_name):
        if first_name in self.contacts:
            del self.contacts[first_name]
            print(f"Deleted all contacts with the first name '{first_name}'.")
        else:
            print(f"No contact found with the first name '{first_name}'.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, contact_list in self.contacts.items():
                print(f"'{name}': [")
                for contact in contact_list:
                    print(f"  {contact}")
                print("]")

    def edit_contacts(self):
        first_name = input("Enter the first name of the contact you want to edit: ")
        if first_name in self.contacts:
            contact = self.contacts[first_name][0]  
            contact.first_name = input("Enter the new first name: ")
            contact.last_name = input("Enter the new last name: ")
            contact.address = input("Enter the new address: ")
            contact.city = input("Enter the new city: ")
            contact.state = input("Enter the new state: ")
            contact.zip_code = input("Enter the new zip code: ")
            contact.phone = input("Enter the new phone number: ")
            contact.email = input("Enter the new email: ")
        else:
            print(f"No contact found with the first name '{first_name}'.")

class AddressBookMain:
    address_book_entry = {}

    def new_address_book(self):
        name = input("Enter the address book name: ")
        if name in self.address_book_entry:
            print("Address book name already exists. Please provide a unique name.")
        else:
            self.address_book_entry[name] = AddressBook()
            print(f"Successfully added the address book '{name}'!")

    def edit_address_book(self, present_name, new_name):
        if present_name in self.address_book_entry:
            self.address_book_entry[new_name] = self.address_book_entry.pop(present_name)
            print(f"Renamed address book from '{present_name}' to '{new_name}'.")
        else:
            print(f"No address book found with the name '{present_name}'.")

    def del_address_book(self, name):
        if name in self.address_book_entry:
            del self.address_book_entry[name]
            print(f"Deleted address book '{name}'.")
        else:
            print(f"No address book found with the name '{name}'.")

    def list_address_books(self):
        if not self.address_book_entry:
            print("No address books exist.")
        else:
            for name in self.address_book_entry:
                print(f"- {name}")

    def get_address_book(self, name):
        return self.address_book_entry.get(name)

class Main:
    def __init__(self):
        self.obj = AddressBookMain()
        self.obj2 = AddressBook()

    def trigger(self):
        while True:
            print("WELCOME TO THE ADDRESS BOOK!")
            print("1. Create a new Address Book")
            print("2. Edit Address Book Name")
            print("3. Delete Address Book")
            print("4. List all Address Books")
            print("5. Work on Address Book")
            print("6. Exit")
            num = int(input("Enter your choice: "))
            match num:
                case 1:
                    self.obj.new_address_book()
                case 2:
                    present_name = input("Enter the current address book name: ")
                    new_name = input("Enter the new address book name: ")
                    self.obj.edit_address_book(present_name, new_name)
                case 3:
                    name = input("Enter the address book name you want to delete: ")
                    self.obj.del_address_book(name)
                case 4:
                    self.obj.list_address_books()
                case 5:
                    name = input("Enter the name of the address book you want to work on: ")
                    address_book = self.obj.get_address_book(name)
                    if address_book:
                        self.manage_address_book(address_book)
                    else:
                        print(f"No address book found with the name '{name}'.")
                case 6:
                    print("Exiting address book application.")
                    break
                case _:
                    print("Invalid choice. Please enter a valid number.")

    def manage_address_book(self, address_book):
        while True:
            print("Managing Address Book!")
            print("1. Add a contact")
            print("2. Delete a contact")
            print("3. Display contacts")
            print("4. Edit a contact")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    address_book.add_contact(
                        first_name=input("Enter the first name: "),
                        last_name=input("Enter the last name: "),
                        address=input("Enter the address: "),
                        city=input("Enter the city: "),
                        state=input("Enter the state: "),
                        zip_code=input("Enter the zip code: "),
                        phone=input("Enter the phone number: "),
                        email=input("Enter the email: ")
                    )
                case 2:
                    first_name = input("Enter the first name of the contact you want to delete: ")
                    address_book.del_contacts(first_name)
                case 3:
                    address_book.display_contacts()
                case 4:
                    address_book.edit_contacts()
                case 5:
                    print("Exiting to main menu.")
                    break
                case _:
                    print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main_app = Main()
    main_app.trigger()
