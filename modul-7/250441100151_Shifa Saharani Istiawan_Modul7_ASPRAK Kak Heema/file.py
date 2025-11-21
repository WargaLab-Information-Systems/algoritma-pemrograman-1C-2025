import json
import os
import re

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists (CONTACTS_FILE):
        with open (CONTACTS_FILE ) as f:
            return json.load(f)
        return
    
def save_contacts():
    with open(CONTACTS_FILE) as f:
        json.dump(contacts, f, indent=4)

contacts = load_contacts()