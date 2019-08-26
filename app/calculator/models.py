from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """  Managing the create and save user actions """
        if not email:
            raise ValueError("User must have a valid email")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Creating the super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports email using instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Operation(models.Model):
    """ Model for the Post"""
    operation_name = models.CharField(max_length=100)
    admin_required = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Operation'

    def __str__(self):
        return self.operation_name

class ReportManager(models.Manager):

    def create_report(self, action_name, action_parameter,
                      user):
        report = self.create(action_name=action_name,
                             action_parameter=action_parameter,
                             user=user)
        return report

class Report(models.Model):
    """ Model for Report"""
    action_name = models.CharField(max_length=100)
    action_parameter = JSONField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='requested_user'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ReportManager()

