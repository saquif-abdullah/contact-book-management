

def WriteContacts(file_name, contacts):

    with open(file_name, 'w') as file:
        for contact in contacts:
            file.write(contact)    

            