from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser


# Create your models here.
class CustomUser(AbstractUser):
    # Add any additional fields here
    is_admin = models.BooleanField(default=False)


