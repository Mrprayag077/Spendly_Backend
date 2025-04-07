import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build credentials from environment variables
cred = credentials.Certificate(
    {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("UNIVERSE_DOMAIN"),
    }
)

# Initialize Firebase app only once
if not firebase_admin._apps:
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
