from app.contact import Contact
from app.storage import Storage


class ContactBook:
    def __init__(self):
        self.storage = Storage()

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.storage.save(contact)

    def show_all(self):
        contacts = self.storage.load_all()
        if not contacts:
            print("bunaqa contact topilmadi.")
        else:
            for i, c in enumerate(contacts, start=1):
                print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")

    def search(self, name):
        contacts = self.storage.load_all()
        found = [c for c in contacts if name.lower() in c["name"].lower()]
        if not found:
            print("bunaqa contact topilmadi")
        else:
            for c in found:
                print(f"{c['name']} - {c['phone']} - {c['email']}")

    def update_or_delete(self, name):
        contacts = self.storage.load_all()
        for i, c in enumerate(contacts):
            if c["name"].lower() == name.lower():
                print(f"Found: {c['name']} - {c['phone']} - {c['email']}")
                action = input("u yozing yangilash uchun d yozing ochirish uchun: ").lower()
                if action == "u":
                    new_phone = input("New phone: ")
                    new_email = input("New email: ")
                    contacts[i]["phone"] = new_phone
                    contacts[i]["email"] = new_email
                    self.storage.overwrite(contacts)
                    print("Contact yangilandi")
                elif action == "d":
                    del contacts[i]
                    self.storage.overwrite(contacts)
                    print("Contact ochirildi.")
                return
        print("bunaqa ismli contact topilmadi.")