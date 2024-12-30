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
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}"


class AddressBook:
    def __init__(self):
        self.contacts = defaultdict(list)

    def add_contact(self, first_name, last_name, address, city, state, zip_code, phone, email):
        new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        if first_name in self.contacts:
            print("A contact with this first name already exists. Please provide a unique name.")
        else:
            self.contacts[first_name] = [new_contact]

    def del_contacts(self):
        first_name = input("Enter the first name of the contact you want to delete: ")
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
        first_name = input("Enter the name of the contact you want to edit: ")
        if first_name in self.contacts:
            new_first_name = input("Enter the first name: ")
            last_name = input("Enter the second name: ")
            address = input("Enter the address: ")
            city = input("Enter the city name: ")
            state = input("Enter the state name: ")
            zip_code = input("Enter the pin code: ")
            phone = input("Enter your mobile number: ")
            email = input("Enter your email: ")
            new_contact = Contact(new_first_name, last_name, address, city, state, zip_code, phone, email)
            self.contacts[first_name].append(new_contact)
        else:
            print("No contact found with the given first name.")

    def search_by_city_or_state(self, city=None, state=None):
        print("\nSearching for persons in city or state...")
        for key,contact_list in self.contacts.items():
            for contact in contact_list:
                if (city and contact.city.lower() == city.lower()) or (state and contact.state.lower() == state.lower()):
                    print(key)       
    
    def view_by_city_or_state(self, city=None, state=None):
        search_results = []
        for contact_list in self.contacts.values():
            for contact in contact_list:
                if (city and contact.city.lower() == city.lower()) or (state and contact.state.lower() == state.lower()):
                    search_results.append(contact)
        if search_results:
            print("Search Results:")
            for contact in search_results:
                print(f"  {contact}")
        else:
            print("No contacts found matching the search criteria.")
    

    def count_by_city_or_state(self, city=None, state=None):
        search_results = []
        for contact_list in self.contacts.values():
            for contact in contact_list:
                if (city and contact.city.lower() == city.lower()) or (state and contact.state.lower() == state.lower()):
                    search_results.append(contact)
        if search_results:
            count=len(search_results)
            print("number of person that belongs same state or city:",count)
        else:
            print("No contacts found matching the search criteria.")


    def sort_by_persons_name(self,address_book_name):
        sorted_entries={}
        for name,contact_list in self.contacts.items():
            sorted_entries[name] = sorted(contact_list, key=lambda contact: (contact.first_name.lower(), contact.last_name.lower()))
        sorted_entries = dict(sorted(sorted_entries.items(), key=lambda item: item[0].lower()))
        for name, contact_list in sorted_entries.items():
            print(f"'{name}': [")
            for contact in contact_list:
                print(f"  {contact}")
            print("]")
            



class AddressBookMain:
    def __init__(self):
        self.address_book_entry = {}

    def new_address_book(self):
        name = input("Enter the address book name: ")
        if name in self.address_book_entry:
            print("An address book with this name already exists. Please provide a unique name.")
        else:
            self.address_book_entry[name] = AddressBook()
            print("Successfully added your address book!")

    def edit_address_book(self, present_name, new_name):
        if present_name in self.address_book_entry:
            self.address_book_entry[new_name] = self.address_book_entry.pop(present_name)
            print(f"Renamed address book from '{present_name}' to '{new_name}'.")
        else:
            print(f"No address book found with the name '{present_name}'.")

    def del_address_book(self, name):
        if name in self.address_book_entry:
            del self.address_book_entry[name]
            print(f"Deleted the address book '{name}'.")
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

    def search_across_address_books(self, city=None, state=None):
        print("\nSearching across all Address Books...")
        results_found = False
        for name, address_book in self.address_book_entry.items():
            print(f"\nSearching in Address Book: {name}")
            address_book.search_by_city_or_state(city=city, state=state)
            results_found = True
        if not results_found:
            print("\nNo Address Books available to search.")
    
    def view_across_address_books(self, city=None, state=None):
        results_found = False
        for name, address_book in self.address_book_entry.items():
            print(f"\nviewing in Address Book: {name}")
            address_book.view_by_city_or_state(city=city, state=state)
            results_found = True
        if not results_found:
            print("\nNo Address Books available to search.")

    def count_across_address_books(self, city=None, state=None):
        results_found = False
        for name, address_book in self.address_book_entry.items():
            print(f"\nviewing in Address Book: {name}")
            address_book.count_by_city_or_state(city=city, state=state)
            results_found = True
        if not results_found:
            print("\nNo Address Books available to search.")
    
    

    def display_all_contacts_in_address_book(self, name):
        """Display all contacts of a specific Address Book."""
        if name in self.address_book_entry:
            print(f"\nDisplaying all contacts in Address Book: {name}")
            address_book = self.address_book_entry[name]
            address_book.display_contacts()
        else:
            print(f"No Address Book found with the name '{name}'.")


class Main:
    def __init__(self):
        self.obj = AddressBookMain()

    def trigger(self):
        while True:
            print("WELCOME TO THE ADDRESS BOOK!!")
            print("--> Enter 1 to create a new Address Book:")
            print("--> Enter 2 to Edit Address Book Name: ")
            print("--> Enter 3 to Delete an Address Book:")
            print('--> Enter 4 to List all Address Books:')
            print('--> Enter 5 to Work on an Address Book:')
            print('--> Enter 6 to Search for a person by City or State:')
            print("--> Enter 7 to view for a person by city or state:")
            print("--> Enter 8 to get number of persons of same city or state:")
            print('--> Enter 9 to Display all Contacts of an Address Book:')
            print("--> Enter 10 to get sorted entries of an particular address book:")
            print('--> Enter 11 to Exit')
            num = int(input("Enter the number: "))
            match num:
                case 1:
                    self.obj.new_address_book()
                case 2:
                    present_name = input("Enter the current address book name: ")
                    new_name = input("Enter the new name for the Address Book: ")
                    self.obj.edit_address_book(present_name, new_name)
                case 3:
                    name = input("Enter the name of the Address Book to delete: ")
                    self.obj.del_address_book(name)
                case 4:
                    self.obj.list_address_books()
                case 5:
                    name = input("Enter the name of the Address Book to work on: ")
                    address_book = self.obj.get_address_book(name)
                    if address_book:
                        self.manage_address_book(address_book)
                    else:
                        print(f"No Address Book found with the name '{name}'.")
                case 6:
                    search_city = input("Enter the city to search (or press Enter to skip): ")
                    search_state = input("Enter the state to search (or press Enter to skip): ")
                    if search_city or search_state:
                        self.obj.search_across_address_books(city=search_city, state=search_state)
                    else:
                        print("You must provide at least a city or a state to search.")
                case 7:
                    city = input("Enter the city to search (or press Enter to skip): ")
                    state = input("Enter the state to search (or press Enter to skip): ")
                    if city or state:
                        self.obj.view_across_address_books(city,state)
                    else:
                        print("You must provide at least a city or a state to search.")
                case 8:
                    city = input("Enter the city to search (or press Enter to skip): ")
                    state = input("Enter the state to search (or press Enter to skip): ")
                    if city or state:
                        self.obj.count_across_address_books(city,state)
                    else:
                        print("You must provide at least a city or a state to search.")
                case 9:
                    address_book_name = input("Enter the name of the Address Book: ")
                    self.obj.display_all_contacts_in_address_book(address_book_name)
                case 10:
                    name = input("Enter the address book name to sort: ")
                    address_book_name = self.obj.get_address_book(name)
                    if address_book:
                        address_book.sort_by_persons_name(address_book_name)
                    else:
                        print(f"No Address Book found with the name '{name}'.")
                case 11:
                    print("Exiting Address Book.")
                    break
                case _:
                    print("Invalid choice. Please enter a valid number.")

    def manage_address_book(self, address_book):
        while True:
            print("Managing Address Book!!")
            print("--> Enter 1 to Add a Contact:")
            print("--> Enter 2 to Delete a Contact:")
            print("--> Enter 3 to Display Contacts:")
            print("--> Enter 4 to Edit a Contact:")
            print("--> Enter 5 to Exit to Main Menu:")
            choice = int(input("Enter the number: "))
            match choice:
                case 1:
                    address_book.add_contact(
                        first_name=input("Enter the first name: "),
                        last_name=input("Enter the second name: "),
                        address=input("Enter the address: "),
                        city=input("Enter the city name: "),
                        state=input("Enter the state name: "),
                        zip_code=input("Enter the pin code: "),
                        phone=input("Enter your Mobile number: "),
                        email=input("Enter your email: ")
                    )
                case 2:
                    address_book.del_contacts()
                case 3:
                    address_book.display_contacts()
                case 4:
                    address_book.edit_contacts()
                case 5:
                    print("Exiting to Main Menu.")
                    break
                case _:
                    print("Invalid choice. Please enter a valid number.")


if __name__ == "__main__":
    main_app = Main()
    main_app.trigger()
