#create a program that stores and manages the contacts in a filename contacts.txt. Each contact entry should include,
#name, phone number and email address.
#Features to implement
            # - Add a new contact
            # - Append a new contact
            # - View and display all contacts
            # - Exit program

# with open("Day06/contacts.txt","w+") as file:
#     file.writelines(["John Doe\n", "07111133322\n","john@doe.com"])

def add_contact(name, phone, email):
    with open("Day06/contacts.txt","a") as file:
        file.write(name+", "+phone +", "+email+"\n")
    print("Contact added successfully!")

def view_contacts():
    with open("Day06/contacts.txt","r") as file:
        contacts = file.read()
        if len(contacts) == 0:
             print("No contacts found!")
             return
        else:
             print(contacts)
                  
def main():
    while True:
        print("\n1. Add a new contact\n2. View all contacts \n3. Exit program")
        choice = int(input("Enter your choice: "))
        
        match choice: 
                    case 1:
                        name = input("Enter name: ")
                        phone = input("Enter phone number: ")
                        email = input("Enter email address: ")
                        add_contact(name, phone, email)
                    case 2:
                        view_contacts()
                    case 3:
                        print("Exiting program...")
                        return
             
main();