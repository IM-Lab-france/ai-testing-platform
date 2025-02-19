from cryptography.fernet import Fernet
import os
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Configuration pour le hachage des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Génération d'une clé pour le chiffrement
encryption_key = os.getenv("ENCRYPTION_KEY", Fernet.generate_key())
cipher_suite = Fernet(encryption_key)

def encrypt_api_key(api_key: str) -> str:
    """
    Chiffre une clé API.

    - **api_key**: La clé API à chiffrer.

    Retourne la clé API chiffrée.
    """
    return cipher_suite.encrypt(api_key.encode()).decode()

def decrypt_api_key(encrypted_api_key: str) -> str:
    """
    Déchiffre une clé API.

    - **encrypted_api_key**: La clé API chiffrée.

    Retourne la clé API déchiffrée.
    """
    return cipher_suite.decrypt(encrypted_api_key.encode()).decode()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Vérifie un mot de passe.

    - **plain_password**: Le mot de passe en clair.
    - **hashed_password**: Le mot de passe haché.

    Retourne True si le mot de passe est correct, sinon False.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hache un mot de passe.

    - **password**: Le mot de passe à hacher.

    Retourne le mot de passe haché.
    """
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Crée un token d'accès JWT.

    - **data**: Les données à encoder dans le token.
    - **expires_delta**: La durée de validité du token.

    Retourne le token JWT.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY", "default_secret_key"), algorithm="HS256")
    return encoded_jwt

def verify_token(token: str) -> dict:
    """
    Vérifie un token JWT.

    - **token**: Le token JWT à vérifier.

    Retourne les données décodées si le token est valide, sinon lève une exception.
    """
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY", "default_secret_key"), algorithms=["HS256"])
        return payload
    except JWTError:
        raise ValueError("Invalid token")