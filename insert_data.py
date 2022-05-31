import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./data/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db= firestore.client()

with open('./data/vocab.json') as f:
    data = json.loads(f.read())
    id = 0
    for level in data.keys():
        for vocab_info in data[level]:
            db.collection(level).document(str(id)).set(vocab_info)
            id += 1