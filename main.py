import json
from datetime import datetime

'''This class is created to initialize the data'''
class Note:
    def __init__(self):
        self.user_id = 0
        self.title = input("Give me title\n")
        self.user_test = input("Give me text\n")
        self.notes = {
            self.user_id: {
                'title': self.title,
                'user_text': self.user_test,
                'date': datetime.now().isoformat()
            }
        }


class Repository:
    def __init__(self):
        self.entries = []

    '''This function loads the data inside the json file'''
    def load_from_json(self, filename):
        with open(filename, 'r') as json_file:
            self.entries = json.load(json_file)

    '''This function saves the data in the json file'''
    def save_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.entries, json_file)

    '''This function deletes the data from the json file'''
    def remove_entry(self, entry_id):
        for entry in self.entries:
            if str(entry_id) in entry:
                self.entries.remove(entry)
                return True
        return False
    
    '''This function edits the data inside the Jason file'''
    def edit_entry(self, entry_id, title, user_text):
        for entry in self.entries:
            if str(entry_id) in entry:
                entry[str(entry_id)]['title'] = title
                entry[str(entry_id)]['user_text'] = user_text
                return True
        return False

'''The list in class Repository contains the input data. This list is stored in the json file. Basically, this list works as DATABASE'''
class JSON:
    def __init__(self, repository, filename):
        self.repository = repository
        self.filename = filename

    def save(self):
        self.repository.save_to_json(self.filename)

    def load(self):
        self.repository.load_from_json(self.filename)

'''User can added data into Notebook with this class'''
class AddCommand:
    def __init__(self, repository):
        self.repository = repository
        self.note = Note()

        self.repository.entries.append(self.note.notes)
        print(self.repository.entries)
        JSON(self.repository, "savedata.json").save()

'''This class calls function "remove entry" from class Repository and the data is deleted'''
class RemoveCommand:
    def __init__(self, repository):
        self.repository = repository
        self.entry_id = input("Enter the ID of the entry you want to remove: ")

        if self.repository.remove_entry(self.entry_id):
            print("Entry removed successfully!")
        else:
            print("Entry not found!")

        JSON(self.repository, "savedata.json").save()

'''This class calls function "edit entry" from class Repositroy and the data is edited'''
class EditCommand:
    def __init__(self, repository):
        self.repository = repository
        self.entry_id = input("Enter the ID of the entry you want to edit: ")
        self.title = input("Enter the new title: ")
        self.user_text = input("Enter the new user text: ")

        if self.repository.edit_entry(self.entry_id, self.title, self.user_text):
            print("Entry edited successfully!")
        else:
            print("Entry not found!")

        JSON(self.repository, "savedata.json").save()

'''This class is created to display the data inside the json file'''
class ViewCommand:
    def __init__(self, repository):
        self.repository = repository

        print(self.repository.entries)

'''Code execution'''
if __name__ == '__main__':
    '''Set command'''
    options = input("""What do you want? 
    If you need to Add data, type 'add data'
    If you need to Remove data, type 'remove data'
    If you need to Edit data, type 'edit data'
    If you need to View data, type 'view data'\n""")
    
    repository = Repository()
    JSON(repository, "savedata.json").load()  # Load data from JSON file

    if options == "add data":
        AddCommand(repository)

    elif options == "remove data":
        RemoveCommand(repository)

    elif options == "edit data":
        EditCommand(repository)

    elif options == "view data":
        ViewCommand(repository)
    
    else:
        print("This command does not exist!!!")