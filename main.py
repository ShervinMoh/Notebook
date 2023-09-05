import json 

# Adde Notebook class
class Notebook:
    def __init__(self):
        self.entries = []

    # We create a dictionary that stores the titles and text inside itself
    def add_entry(self, title, user_text):
        entry = {
            'title': title,
            'user_text': user_text
        }
        self.entries.append(entry)

    # We create this  function for save datas into json file
    def save_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.entries, json_file)