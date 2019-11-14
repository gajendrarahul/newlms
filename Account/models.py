from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser
)
# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self,email, is_student=False,is_teacher=False,is_suspended=False, is_firstLogin=True, password=None):
        if not email:
            raise ValueError("user must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            is_student=is_student,
            is_teacher=is_teacher,
            is_suspended=is_suspended,
            is_firstLogin=is_firstLogin,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        user = self.create_user(
            email, password=password
        )
        user.is_firstLogin = False
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=225,
        unique=True,
     )
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    is_firstLogin = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

    def issuspended(self):
        return self.is_suspended

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin