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