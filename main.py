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
           pass
        else:
            self.contacts[first_name]=[new_contact]
    
    def del_contacts(self,first_name):
        first_name=input("Enetr the first_name you want to delete:")
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
        first_name=input("Enter the name you want to edit contacts:")
        if first_name in self.contacts:
            first_name=input("Enter the first name:"),
            last_name=input("Enter the second name:"),
            address=input("Enter the  address:"),
            city=input("Enter the city name:"),
            state=input("Enter the state name:"),
            zip_code=input("Enter the pin code:"),
            phone=input("Enter your Mobile number:"),
            email=input("Enter your email:")
            new_contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
            self.contacts[first_name].append(new_contact)
        else:
            pass



class AddressBookMain:
    address_book_entry={}
    
    def new_address_book(self):
        name=input("Enter the adrress book name:")
        if name in self.address_book_entry:
              print("give unique address name")
        else:
          self.address_book_entry[name] = AddressBook()
          print("successfully added your address book!!")
    def edit_addres_book(self,present_name,new_name):
        
        if present_name in self.address_book_entry:
            # my_dict['location'] = my_dict.pop('city')
            self.address_book_entry[new_name]=self.address_book_entry.pop(present_name)
            print(f"Renamed address book from '{present_name}' to '{new_name}'.")
        else:
            print(f"No Address Book found with this {present_name}")
    def del_address_book(self,name):
        if name in self.address_book_entry:
                del self.address_book_entry[name]
        else:
            print(f"No Address Book found with this {name}")
    def list_address_books(self):
     if not self.address_book_entry:
        print("No address books exist.")
     else:
        for name in self.address_book_entry:
            print(f"- {name}")
    def get_address_book(self,name):
       return self.address_book_entry.get(name)


class main:
    def __init__(self):
        self.obj=AddressBookMain()
        self.obj2=AddressBook()

    def triger(self):
        while True:
            print("WELCOME TO THE ADDRESS BOOK!!")
            print("--> Enter 1 to create an new Address Book:")
            print("--> Enter 2 to Edit Address Book Name: ")
            print("--> Enter 3 Delete address book:")
            print('--> Enter 4 to list all address book:')
            print('--> Enter 5 to work on address book:')
            print('--> Enter 6 if you want to exit')
            num=int(input("Enter the number:"))      
            match num:
                    case 1:
                     self.obj.new_address_book()
                    case 2:
                     present_name=input("Enter the current address book name:")
                     new_name=input("Enter the name to the Address book:")
                     self.obj.edit_addres_book(present_name,new_name)
                    case 3:
                     name=input("enter name which address book you want ot delete: ")
                     self.obj.del_address_book(name)
                    case 4:
                     self.obj.list_address_books()
                    case 5:
                      name=input("Enter the name of the Address book you want to work on:")
                      address_book=self.obj.get_address_book(name)
                      if address_book:
                         self.manage_addres_book(address_book)
                      else:
                         print(f'no address book found on this {name}.')
                    case 6:
                      print("exiting address book: ")
                      break
                    case _:
                      print("Ivalid choice.please enter the valid number:")



    def manage_addres_book(self, address_book):
       while True:

        print("Mangeing address book!!")
        print("--> Enter 1 add a conatact:")
        print("--> Enter 2 to Delete a contact:")
        print("--> Enter 3 to Display the contacts:")
        print("--> Enter 4 to edit the contacts ")
        print("--> Enter 5 to exit from contacts:")
        

        choice=int(input("Enter the number:"))
        
        match choice:
            case 1:
               self.obj2.add_contact(
                        first_name=input("Enter the first name:"),
                        last_name=input("Enter the second name:"),
                        address=input("Enter the  address:"),
                        city=input("Enter the city name:"),
                        state=input("Enter the state name:"),
                        zip_code=input("Enter the pin code:"),
                        phone=input("Enter your Mobile number:"),
                        email=input("Enter your email:")
                        )
            case 2:
               self.obj2.del_contacts()
            case 3:
              self.obj2.display_contacts()
            case 4:
              self.obj2.edit_contacts()  
            case 5:
               print("exiting to main menu")
               break 
            case _:
              print("Invalid choice ,, plaese give valid choice!!")

if __name__=="__main__":
    main_app=main()
    main_app.triger()
    




