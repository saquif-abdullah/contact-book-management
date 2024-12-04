
import read_contacts
import menu_call


def View(file_name):
    contacts = read_contacts.ReadContacts(file_name)
    
    print("\n\n============================")
    print("       __All Contacts__     ")
    print("============================\n\n")

    ids = ["Name         :", "Email        :", "Phone Number :", "Address      :"]

    for i in range(len(contacts)):
       print(f"  {i+1}.")
       parts = contacts[i].split(",")
       
       for i in range(len(parts)):
           part = parts[i]

           if part[0] == ' ':
               part = part[1:]
           print("   ",ids[i], part)
    
    menu_call.Call()