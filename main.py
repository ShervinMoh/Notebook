import json 

# Adde Notebook class
class Notebook:
    def __init__(self):
        self.entries = []

    # We create a dictionary that stores the titles and text inside itself
    def add_entry(self, ID, title, user_text):
        entry = {
            'ID' : ID,
            'title': title,
            'user_text': user_text
        }
        self.entries.append(entry)

    # We create this  function for save datas into json file
    def save_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.entries, json_file)

    # Display in IDLE what user add into notebook
    def display_entries(self):
        if not self.entries:
            print("No entries found!")
            return

        # Create for loop for print title and text into IDLE
        for entry in self.entries:
            title = entry['title']
            user_text = entry['user_text']
            print("Title:", title)
            print("User Text:", user_text)
            print()

notebook = Notebook()

# Added input for get values from user
num_entries = int(input("Enter the number of entries you want to add: "))

for i in range(num_entries):
    title = input("Enter the entry title: ")
    user_text = input("Enter the user text: ")
    notebook.add_entry(i, title, user_text)

# Execute the code
notebook.save_to_json("savedata.json")
notebook.display_entries()