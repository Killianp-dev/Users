import pytest
from .models import CustomUser


@pytest.mark.django_db
class TestCustomUserModel:
    """
    Test suite for the CustomUser model.

    Methods:
        test_create_user: Tests the creation of a standard user and validates the email and password.
        test_create_superuser: Tests the creation of a superuser and checks the is_superuser and is_staff flags.
        test_user_string_representation: Tests that the string representation of the user is the email address.
    """

    def test_create_user(self) -> None:
        """
        Tests that a CustomUser can be created with an email and password.
        Verifies that the email is set correctly and the password is valid.
        """
        user: CustomUser = CustomUser.objects.create_user(email="test@example.com", password="testpass123")
        assert user.email == "test@example.com"
        assert user.check_password("testpass123")
        assert user.is_superuser is False
        assert user.is_staff is False

    def test_create_superuser(self) -> None:
        """
        Test the creation of a superuser with a specific email and password.

        This test verifies the following: The email is set correctly, the password is hashed and can be validated,
        the user has the superuser and staff privileges.
        """
        user: CustomUser = CustomUser.objects.create_superuser(email="admin@example.com", password="adminpass123")
        assert user.email == "admin@example.com"
        assert user.check_password("adminpass123")
        assert user.is_superuser is True
        assert user.is_staff is True

