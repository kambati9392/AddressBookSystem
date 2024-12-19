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
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state} - {self.zip_code}, Phone: {self.phone}, Email: {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, address, city, state, zip_code, phone, email):
        new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        self.contacts.append(new_contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

address_book = AddressBook()

