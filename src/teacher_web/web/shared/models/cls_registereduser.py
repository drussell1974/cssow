from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from shared.models.core.basemodel import BaseModel, BaseDataAccess, try_int

# TODO: 206 inherit RegisteredUserForm from UserCreationForm - this model may not be required
class RegisteredUserManager(BaseUserManager):
    
    def create_user(self, data, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        
        user = self.model(
            email=self.normalize_email(model.email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


# TODO: 206 inherit RegisteredUserForm from UserCreationForm - this model may not be required
class RegisteredUserModel(BaseModel):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = RegisteredUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __init__(self, id = 0, first_name = "", last_name = "", created = "", created_by_id = 0, created_by_name = "", is_from_db=False):
        super().__init__(id_= id, display_name = "{} {}".format(first_name, last_name), created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=0, is_from_db=is_from_db)

        self.is_valid = False
        self.validation_errors = {}
        is_valid = True

    def _clean_up(self):
        self.first_name = first_name.trim(" ")
        self.last_name = last_name.trim(" ")
        self.email = email.trim(" ")


    def is_new(self):
        return True if self.id == 0 else False
    

    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate first_name
        self._validate_required_string("first_name", self.first_name, 1, 30)

        # Validate last_name
        self._validate_required_string("last_name", self.last_name, 1, 30)

        # Validate summary
        self._validate_required_string("email", self.summary, 1, 80)

        return self.is_valid


