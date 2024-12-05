
import read_contacts
import write_contacts
import menu_call
import clear

def Delete(file_name):
    clear.Clear()
    contacts = read_contacts.ReadContacts(file_name)
    
    print("\n\n___________Delete Contact___________\n\n")

    
    key = input("  Enter name or Email or Phone or Address to Delete the contact : ")
    ids = ["Name         :", "Email        :", "Phone Number :", "Address      :"]

    for contact in contacts:
       parts = contact.split(",")
       
       for part in parts:
           if part[0] == ' ':
                part = part[1:]

           if(part == key):
                
                for j in range(len(parts)):
                    p = parts[j]

                    if p[0] == ' ':
                        p = p[1:]
                    print("   ",ids[j], p)
                
                yn = input("\n  Do you want to delete it (Y/N) : ")
                if yn == 'Y' or yn =='y':
                    contacts.remove(contact)
                    print("  Contact Deleted Succussfully\n\n")
                


    write_contacts.WriteContacts(file_name, contacts)
       
    menu_call.Call()