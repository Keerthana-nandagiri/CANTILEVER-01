contacts = []

def add():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append([name, phone, email])
    print("Contact added!")

def update():
    listall()
    if len(contacts) == 0:
        print("No contacts to update.")
        return
    num = int(input("Enter contact number to update: "))
    if num < 0 or num >= len(contacts):
        print("Invalid contact number!")
        return
    name = input("Enter new name (leave blank to keep same): ")
    phone = input("Enter new phone (leave blank to keep same): ")
    email = input("Enter new email (leave blank to keep same): ")

    if name != "":
        contacts[num][0] = name
    if phone != "":
        contacts[num][1] = phone
    if email != "":
        contacts[num][2] = email

    print("Contact updated!")

def delete():
    listall()
    if len(contacts) == 0:
        print("No contacts to delete.")
        return
    num = int(input("Enter contact number to delete: "))
    if num < 0 or num >= len(contacts):
        print("Invalid contact number!")
        return
    contacts.pop(num)
    print("Contact deleted!")

def listall():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("---- Contacts ----")
        for i, c in enumerate(contacts):
            if len(c) == 3:
                print(i, c[0], "-", c[1], "-", c[2])
            else:
                print(i, c)  

while True:
    print("\n1) Add  2) Update  3) List  4) Delete  5) Quit")
    choice = input("Pick: ")

    if choice == "1":
        add()
    elif choice == "2":
        update()
    elif choice == "3":
        listall()
    elif choice == "4":
        delete()
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid choice.")
