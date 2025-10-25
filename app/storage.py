import json
import os
from app.contact import Contact


class Storage:
    def __init__(self):
        self.filename = "database/contacts.json"
        os.makedirs("database", exist_ok=True)

    def load_all(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save(self, contact: Contact):
        contacts = self.load_all()
        contacts.append(contact.to_dict())

        with open(self.filename, "w") as f:
            json.dump(contacts, f, indent=4)

    def overwrite(self, contacts):
       
        with open(self.filename, "w") as f:
            json.dump(contacts, f, indent=4)
