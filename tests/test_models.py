import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import User


def test_create_user(db_session):
    """Test creating a user in the database."""
    user = User(
        username="testuser",
        email="test@example.com",
        hashed_password="hashedpassword123",
    )

    db_session.add(user)
    db_session.commit()

    retrieved_user = db_session.query(User).filter(User.username == "testuser").first()

    assert retrieved_user is not None
    assert retrieved_user.username == "testuser"
    assert retrieved_user.email == "test@example.com"
    assert retrieved_user.hashed_password == "hashedpassword123"


def test_user_repr(db_session):
    """Test the string representation of a user."""
    user = User(
        username="testuser",
        email="test@example.com",
        hashed_password="hashedpassword123",
    )

    assert "testuser" in str(user)
    assert "test@example.com" in str(user)
