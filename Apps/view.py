
import read_contacts
import menu_call
import clear

def View(file_name):
    clear.Clear()
    contacts = read_contacts.ReadContacts(file_name)
    
    print("\n\n___________View All Contact___________\n\n")

    ids = ["Name         :", "Email        :", "Phone Number :", "Address      :"]

    for i in range(len(contacts)):
       print(f"  {i+1}.")
       parts = contacts[i].split(",")
       
       for j in range(len(parts)):
           part = parts[j]

           if part[0] == ' ':
               part = part[1:]
           print("   ",ids[j], part)
    
    menu_call.Call()