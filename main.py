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