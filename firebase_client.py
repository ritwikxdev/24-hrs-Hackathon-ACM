import firebase_admin
from firebase_admin import credentials, firestore

# 1) Point to your Firebase service account JSON
#    Put the downloaded key file in this folder and
#    rename it to: serviceAccount.json
cred = credentials.Certificate("serviceAccount.json")

# 2) Initialize Firebase Admin
firebase_admin.initialize_app(cred)

# 3) Create a Firestore client
db = firestore.client()

def _clean_doc(raw: dict) -> dict:
    """
    Normalize a raw Firestore document:
    - Strip whitespace from all field KEYS  (e.g. 'hospitalName ' → 'hospitalName')
    - Strip whitespace from all string VALUES (e.g. ' Apollo Hospital' → 'Apollo Hospital')
    - If a string value equals its own key name (corrupted placeholder), replace with None
    """
    cleaned = {}
    for k, v in raw.items():
        clean_key = k.strip()
        if isinstance(v, str):
            clean_val = v.strip()
            # Guard against placeholder values like {"billedAmount": "billedAmount"}
            if clean_val == clean_key or clean_val == "":
                clean_val = None
        else:
            clean_val = v
        cleaned[clean_key] = clean_val
    return cleaned

def load_claims():
    """Read all claim documents from the 'claims' collection."""
    snap = db.collection("claims").stream()
    claims = []
    for doc in snap:
        item = _clean_doc(doc.to_dict())
        item["id"] = doc.id
        claims.append(item)
    return claims
