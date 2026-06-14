import hashlib
import time
import os

def generate_transaction_id(user_id: str):
    data = f"{user_id}-{time.time()}-{os.urandom(8).hex()}"
    return hashlib.sha256(data.encode()).hexdigest()


def process_payment(user_id, amount):
    transaction_id = generate_transaction_id(user_id)

    print("Processing payment...")
    print(f"Transaction ID: {transaction_id}")
    print(f"Amount: {amount}")

    if amount > 1000:
        return {"status": "flagged", "transaction_id": transaction_id}

    return {"status": "approved", "transaction_id": transaction_id}