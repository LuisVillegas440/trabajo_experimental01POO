import json
import os

class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        if not os.path.exists(self.file_name):
            return []
        
        with open(self.file_name, "r", encoding="utf-8") as file:
            return json.load(file)
        
    def save(self, data):

        directory = os.path.dirname(self.file_name)
        
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)