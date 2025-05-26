import json
from datetime import datetime
import os

DATA_FILE = "savedata.json"

class Note:
    def __init__(self, title, user_text):
        self.user_id = int(datetime.now().timestamp())
        self.title = title
        self.user_text = user_text
        self.date = datetime.now().isoformat()
        
    def to_dict(self):
        return {
            str(self.user_id): {
                'title': self.title,
                'user_text': self.user_text,
                'date': self.date
            }
        }

class Repository:
    def __init__(self):
        self.entries = []
        self.load_from_json(DATA_FILE)

    def load_from_json(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as json_file:
                try:
                    self.entries = json.load(json_file)
                except json.JSONDecodeError:
                    self.entries = []
        else:
            self.entries = []

    def save_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.entries, json_file, indent=4)

    def add_note(self, note):
        self.entries.append(note.to_dict())
        self.save_to_json(DATA_FILE)

    def remove_entry(self, entry_id):
        for entry in self.entries:
            if str(entry_id) in entry:
                self.entries.remove(entry)
                self.save_to_json(DATA_FILE)
                return True
        return False
    
    def edit_entry(self, entry_id, title, user_text):
        for entry in self.entries:
            if str(entry_id) in entry:
                entry[str(entry_id)]['title'] = title
                entry[str(entry_id)]['user_text'] = user_text
                entry[str(entry_id)]['date'] = datetime.now().isoformat()
                self.save_to_json(DATA_FILE)
                return True
        return False

    def get_all_notes(self):
        return self.entries