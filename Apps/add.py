
import read_contacts
import write_contacts
import menu_call
import clear

def Add(file_name):

    clear.Clear()
    print("\n\n___________Add Contact___________\n\n")

    contact = {}
    contact["name"] = input("    Enter Name : ")
    contact["email"] = input("    Enter Email : ")
    contact["phone"] = input("    Enter Phone Number : ")
    contact["address"] = input("    Enter Address : ")

    print(("\n\n    1. Save Contact\n    2. Cancel"))
    key = int(input("\n    Choose an option : "))
    if key == 2:
        return

    contact_in_line =  f"{contact["name"]}, {contact["email"]}, {contact["phone"]}, {contact["address"]}\n"
    contacts = read_contacts.ReadContacts(file_name)
    contacts.append(contact_in_line)

    write_contacts.WriteContacts(file_name, contacts)
    print("    Contact Saved Successfully")

    menu_call.Call()
    