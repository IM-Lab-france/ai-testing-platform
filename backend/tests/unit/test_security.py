import pytest
from src.core.security import encrypt_api_key, decrypt_api_key, verify_password, get_password_hash, create_access_token, verify_token
from jose import jwt
from datetime import timedelta

def test_encrypt_decrypt_api_key():
    api_key = "my_secret_api_key"
    encrypted = encrypt_api_key(api_key)
    decrypted = decrypt_api_key(encrypted)
    assert decrypted == api_key

def test_password_hashing():
    password = "my_password"
    hashed = get_password_hash(password)
    assert verify_password(password, hashed)
    assert not verify_password("wrong_password", hashed)

def test_create_access_token():
    data = {"sub": "testuser"}
    token = create_access_token(data, expires_delta=timedelta(minutes=10))
    payload = verify_token(token)
    assert payload["sub"] == "testuser"

def test_verify_token():
    data = {"sub": "testuser"}
    token = create_access_token(data)
    with pytest.raises(ValueError):
        verify_token("invalid_token")