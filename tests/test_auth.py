import jwt
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from auth import create_access_token, verify_password, get_password_hash


def test_password_hashing():
    """Test password hashing and verification."""
    password = "securepassword123"
    hashed = get_password_hash(password)
    assert verify_password(password, hashed)
    assert not verify_password("wrongpassword", hashed)


def test_create_access_token():
    """Test JWT token creation."""
    user_id = 123
    token = create_access_token({"sub": str(user_id)})

    assert isinstance(token, str)
    decoded = jwt.decode(token, options={"verify_signature": False})

    assert decoded["sub"] == str(user_id)
    assert "exp" in decoded
