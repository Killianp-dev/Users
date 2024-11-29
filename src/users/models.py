from __future__ import annotations

from typing import Optional, TypeVar

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


CustomUserType = TypeVar("CustomUserType", bound="CustomUser")


class CustomUserManager(BaseUserManager[CustomUserType]):
    """Manager class for handling the creation of custom users and superusers.

    This manager provides methods for creating both regular users and superusers,
    ensuring that the necessary fields and settings are applied.

    Methods:
        create_user(email: str, password: Optional[str] = None) -> CustomUserType:
            Creates and returns a regular user with the given email and password.

        create_superuser(email: str, password: Optional[str] = None) -> CustomUserType:
            Creates and returns a superuser with the given email and password, setting
            additional privileges.
    """
    def create_user(self, email: str, password: Optional[str] = None) -> CustomUserType:
        """Creates and returns a regular user with the given email and password.

        Args:
            email (str): The email address for the user. Must be provided.
            password (Optional[str], optional): The password for the user. Defaults to None for more flexibility.

        Raises:
            ValueError: If the email is not provided.

        Returns:
            CustomUser: The created user instance.
        """
        if not email:
            raise ValueError("Le champ email est obligatoire")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: Optional[str] = None) -> CustomUserType:
        """Creates and returns a superuser with the given email and password.

        This method sets the `is_staff` and `is_superuser` flags to True.

        Args:
            email (str): The email address for the superuser. Must be provided.
            password (Optional[str], optional): The password for the superuser. Defaults to None.

        Returns:
            CustomUser: The created superuser instance.
        """
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model that uses email as the unique identifier instead of username.

    Inherits from `AbstractBaseUser` and `PermissionsMixin` and provides custom fields like `zip_code`,
    along with the standard `is_active`, `is_staff`, and `is_superuser` flags.

    Attributes:
        email: The user's email address, unique and required.
        is_active: Indicates whether the user account is active. Defaults to True.
        is_staff: Indicates whether the user can access the admin site. Defaults to False.
        is_superuser: Indicates whether the user has all permissions without explicitly assigning them. Defaults to False.
        zip_code: Optional field to store the user's zip code.
    """
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    zip_code = models.CharField(blank=True, max_length=5)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Returns the string representation of the user, which is the email address.

        Returns:
            str: The user's email address.
        """
        return self.email

    class Meta:
        """Meta options for the CustomUser model.

        Options:
            verbose_name (str): The singular name to use for this model in the admin
                interface. Defaults to 'utilisateur'.
        """
        verbose_name = "utilisateur"
