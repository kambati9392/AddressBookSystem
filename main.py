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
        self.contacts =defaultdict(list)

    def add_contact(self, first_name, last_name, address, city, state, zip_code, phone, email):
        new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        if first_name in self.contacts:
           self.contacts[first_name].append(new_contact)
        else:
            self.contacts[first_name]=[new_contact]
    
    def del_contacts(self,first_name):
        if first_name in self.contacts:
              del self.contacts[first_name]
  
    def display_contacts(self):
     for name, contact_list in self.contacts.items():
        print(f"'{name}': [")
        for contact in contact_list:
            print(f"  {contact}")
        print("]")
   


address_book = AddressBook()

while True:
    str1=input(" if you want to add contacts , enter add | don't want means enter no : ")
    if str1 == "add":
            address_book.add_contact(
            first_name=input("Enter the first name:"),
            last_name=input("Enter the second name:"),
            address=input("Enter the  address:"),
            city=input("Enter the city name:"),
            state=input("Enter the state name:"),
            zip_code=input("Enter the pin code:"),
            phone=input("Enter your Mobile number:"),
            email=input("Enter your email:")
            
            # first_name="ram",
            # last_name="reddy",
            # address="1/15",
            # city="kurnool",
            # state="AP",
            # zip_code="54321",
            # phone="12345678",
            # email="ram@gmail.com"
            )
            print("successfully addded contacts!!")
    else:
     break
while True:
    str1=input(" if you want to delete contacts ,, enter delete | don't want means ,, enter no: ")
    if str1 == "delete":
      address_book.del_contacts(
            first_name=input("enter the first_name you want to delete from contacts:")
        )
    else:
        break


address_book.display_contacts()


