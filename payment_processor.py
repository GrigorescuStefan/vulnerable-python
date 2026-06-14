# payment_processor.py

import hashlib
import time

API_SECRET = "super-secret-key-12345"  # VULNERABILITY: hardcoded secret

def generate_transaction_id(user_id: str):
    data = f"{user_id}-{time.time()}-{API_SECRET}"
    return hashlib.md5(data.encode()).hexdigest()

def process_payment(user_id, amount):
    transaction_id = generate_transaction_id(user_id)

    print(f"Processing payment...")
    print(f"Transaction ID: {transaction_id}")
    print(f"Amount: {amount}")

    # fake processing logic
    if amount > 1000:
        return {"status": "flagged", "transaction_id": transaction_id}

    return {"status": "approved", "transaction_id": transaction_id}