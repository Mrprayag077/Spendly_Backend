import firebase_admin
from firebase_admin import credentials, db
import os

# Build path to JSON key
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cred_path = os.path.join(BASE_DIR, "serviceAccountKey.json")

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(
        cred, {"databaseURL": "https://spendly-e467c-default-rtdb.firebaseio.com"}
    )

def get_user_data(user_uuid):
    ref = db.reference(f"users/{user_uuid}")
    return ref.get()


def create_or_update_user(user_uuid, user_data):
    ref = db.reference(f"users/{user_uuid}")
    ref.update(user_data)
    return ref.get()


def add_transaction(user_uuid, transaction_id, transaction_data):
    ref = db.reference(f"users/{user_uuid}/transactions/{transaction_id}")
    ref.set(transaction_data)
    return ref.get()


def edit_transaction(user_uuid, transaction_id, transaction_data):
    ref = db.reference(f"users/{user_uuid}/transactions/{transaction_id}")
    ref.update(transaction_data)
    return ref.get()


def delete_transaction(user_uuid, transaction_id):
    ref = db.reference(f"users/{user_uuid}/transactions/{transaction_id}")
    ref.delete()
