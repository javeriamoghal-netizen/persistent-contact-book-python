1
import os

FILENAME = "contacts.txt"

contacts = {}

# -------- LOAD CONTACTS FROM FILE --------
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            contacts[name] = phone


# -------- FUNCTION TO SAVE CONTACTS --------
def save_contacts():
    with open(FILENAME, "w") as file:
        for name in contacts:
            file.write(name + "," + contacts[name] + "\n")


# -------- MAIN PROGRAM --------
while True:
    print("\n---- CONTACT BOOK ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        save_contacts()
        print("Contact saved successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\nYour Contacts:")
            for name in contacts:
                print(name, ":", contacts[name])

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print("Phone number:", contacts[search])
        else:
            print("Contact not found.")

    elif choice == "4":
        delete = input("Enter name to delete: ")
        if delete in contacts:
            del contacts[delete]
            save_contacts()
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")