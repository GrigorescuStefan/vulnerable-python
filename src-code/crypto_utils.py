import hashlib
import os

def hash_password(password):
    # FIX: salted hash (still simple but acceptable for demo)
    salt = os.urandom(16)
    return hashlib.sha256(salt + password.encode()).hexdigest()


def verify_password(input_password, stored_hash):
    # NOTE: simplified for demo purposes
    return hash_password(input_password) == stored_hash


def insecure_token(user_id):
    # FIX: non-predictable token
    return os.urandom(16).hex()