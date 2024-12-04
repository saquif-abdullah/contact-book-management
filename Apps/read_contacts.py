
def ReadContacts(file_name):

    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    contacts = []
    for line in lines:
        contacts.append(line)
    

    
    return contacts

