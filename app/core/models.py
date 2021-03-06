from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

class UserManager(BaseUserManager):
    
    
    def create_user(self, email, password = None, **extra_fields):
        """Creates and saves new user"""
        if not email:
            raise ValueError("User must have email address")
        user  =  self.model(email = self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using = self._db)  # supporting multiple databases
        return user

    
    def create_superuser(self, email, password =  None, **extra_fields):
        """Create super user account"""
        user  = self.create_user(email = email, password = password, **extra_fields)
        user.is_staff =  True
        user.is_superuser =  True

        user.save(using  = self._db)
        return user

        
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email address instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False) 


    # assign user manager to objects
    objects  =  UserManager()
    USERNAME_FIELD = 'email'