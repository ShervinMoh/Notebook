import json
from datetime import datetime

# Adde Notebook class
class Notebook:
    def __init__(self):
        self.entries = []

    # We create a dictionary that stores the titles and text inside itself
    def add_entry(self, ID, title, user_text):
        entry = {
            'ID': ID,
            'title': title,
            'user_text': user_text,
            'date': datetime.now().isoformat()
        }
        self.entries.append(entry)

    # We create this  function for save datas into json file
    def save_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.entries, json_file)

    # Clear notebook
    def clear_all(self):
        for entry in self.entries:
            self.entries.remove(entry)
        print("Notebook has been cleared") 

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

elif menu == "clear":
    notebook.clear_all()
    notebook.save_to_json("savedata.json")
    notebook.display_entries()

else:
    print("Check the command you have chosen")