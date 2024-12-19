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
        self.contacts = {}

    def add_contact(self, first_name, last_name, address, city, state, zip_code, phone, email):
        new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        self.contacts[first_name]=[new_contact]

   
    def display_contacts(self):
     for name, contact_list in self.contacts.items():
        print(f"'{name}': [")
        for contact in contact_list:
            print(f"  {contact}")
        print("]")
    
     


address_book = AddressBook()

address_book.add_contact(
    first_name=input("Enter the first name:"),
    last_name=input("Enter the second name:"),
    address=input("Enter the  address:"),
    city=input("Enter the city name:"),
    state=input("Enter the state name:"),
    zip_code=input("Enter the pin code:"),
    phone=input("Enter your Mobile number:"),
    email=input("Enter your email:")
)


address_book.display_contacts()
