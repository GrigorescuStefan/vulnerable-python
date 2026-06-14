# crypto_utils.py

import hashlib

def hash_password(password):
    # VULNERABILITY: weak hashing (MD5, no salt)
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(input_password, stored_hash):
    return hash_password(input_password) == stored_hash


def insecure_token(user_id):
    # predictable token generation
    return hashlib.md5(str(user_id).encode()).hexdigest()