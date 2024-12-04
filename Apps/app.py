
import add
import view
import search
import edit
import delete


class ContactManager:      ### Used OOP for my own satisfiction though it is not ordered to do
         
    def __init__(self):
   
        self.file_name = "../Dataset/contacts.csv"
        
        menu = {
            1: "Add New Contact",
            2: "View All Contacts",
            3: "Search Contact",
            4: "Edit Contact",
            5: "Delete Contact",
            6: "Exit"
        }

        print("\n\n============================")
        print("          _DhumkeTU_        ")
        print("      __Contact Manager__   ")
        print("============================")
        
        k = int(input("\n\n\n  Pres 1 to Enter : "))
        if k != 1:
            exit()

        

        while True:

            print("\n\n============================")
            print("          _Main Menu_        ")
            print("============================\n\n")
            
            for i, msg in menu.items():
                print(f"    {i}. {msg}\n")
            
            key = int(input("    Choose an Option  :  "))
            
            if key == 1:
                self.Add()
            elif key == 2:
                self.View()
            elif key == 3:
                self.Search()
            elif key == 4:
                self.Edit()
            elif key == 5:
                self.Delete()
            elif key == 6:
                exit()
            else:
                print("Invalid Input")
            print("\n\n")
        
    
    def Add(self):
        add.Add(self.file_name)
    
    def View(self):
        view.View(self.file_name)
    
    def Search(self):
        search.Search(self.file_name)
    
    def Edit(self):
        edit.Edit(self.file_name)
    
    def Delete(self):
        delete.Delete(self.file_name)

    def Search(self):
        search.Search(self.file_name)



if __name__=="__main__":
    ContactManager()

    

