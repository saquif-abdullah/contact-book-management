
import add
import remove
import search


class ContactManager:      ### Used OOP for my own satisfiction though it is not ordered to do
    
    def __init__(self):
        menu = {
            0: "Exit",
            1: "Add",
            2: "Remove",
            3: "Search",
        }

        while True:
            for i, msg in menu.items():
                print(f"{i} for {msg}")
            
            key = int(input())
            if key == 0:
                exit()
            elif key == 1:
                self.Add()
            elif key == 2:
                self.Remove()
            elif key == 3:
                self.Search()
            else:
                print("Invalid Input")
    
    def Add(self):
        add.Add()
    
    def Remove(self):
        remove.Remove()
    
    def Search(self):
        search.Search()



if __name__=="__main__":
    ContactManager()

    

