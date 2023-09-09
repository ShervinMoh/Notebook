import json
from datetime import datetime

'''This class is created to initialize the data'''
class Note:
    def __init__(self):
        self.user_id = 0
        self.title = None
        self.user_test = None

'''The input data is put into the list in this class'''
class Repository:
    def __init__(self):
        self.entries = []

'''The list in class Repository contains the input data. This list is stored in the json file. Basically, this list works as DATABASE'''
class JSON:
    def __init__(self, repository, filename):
        self.repository = repository
        self.filename = filename
        with open(filename, 'w') as json_file:
            json.dump(self.repository.entries, json_file)

'''UIser can added data into Notebook with this class'''
class AddCommand:
    def __init__(self, repository):
        self.repository = repository
        self.note = Note()
        self.note.title = input("Give me title\n")
        self.note.user_test = input("Give me text\n")
        notes = {
            self.note.user_id: {
                'title': self.note.title,
                'user_text': self.note.user_test,
                'date': datetime.now().isoformat()
            }
        }
        self.repository.entries.append(notes)
        print(self.repository.entries)
        JSON(self.repository, "savedata.json")

# Adde Notebook class
class Notebook:
    # We create a dictionary that stores the titles and text inside itself
    def add_entry(self, ID, title, user_text):
        entry = {
            'ID': ID,
            'title': title,
            'user_text': user_text,
            'date': datetime.now().isoformat()
        }
        self.entries.append(entry)

notebook = Notebook()

menu = input("""What do you want? 
            If you need to add data, type 'add data'
            If you need to clear notebook, type 'clear'\n""")

if menu == "add data":
    # Added input for getting values from the user
    num_entries = int(input("Enter the number of entries you want to add: "))

    for i in range(num_entries):
        title = input("Enter the entry title: ")
        user_text = input("Enter the user text: ")
        notebook.add_entry(i, title, user_text)

    # Execute the code
    notebook.save_to_json("savedata.json")
    notebook.display_entries()

else:
    print("Check the command you have chosen")