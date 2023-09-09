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

'''The input data is put into the list in this class'''
class Repository:
    def __init__(self):
        self.entries = []

    def load_from_json(self, filename):
        with open(filename, 'r') as json_file:
            self.entries = json.load(json_file)

    def save_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.entries, json_file)

    def remove_entry(self, entry_id):
        for entry in self.entries:
            if str(entry_id) in entry:
                self.entries.remove(entry)
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

'''UIser can added data into Notebook with this class'''
class AddCommand:
    def __init__(self, repository):
        self.repository = repository
        self.note = Note()

        self.repository.entries.append(self.note.notes)
        print(self.repository.entries)
        JSON(self.repository, "savedata.json").save()

'''Code execution'''
if __name__ == '__main__':
    '''Set command'''
    options = input("What do you want? If you need to add data, type 'add data': \n")
    
    repository = Repository()
    JSON(repository, "savedata.json").load()  # Load data from JSON file

    if options == "add data":
        AddCommand(repository)
    
    else:
        print("This command does not exist!!!")