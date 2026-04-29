from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser



phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be entered in the format: '+998xxxxxxxxx'. Up to 9 digits allowed."
)


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email, password=None, **extra_fields):  # email qo'shildi
        if not phone_number:
            raise ValueError('The Phone Number must be set')
        if not email:  # Emailni tekshirish
            raise ValueError('The Email must be set')

        email = self.normalize_email(email)  # Emailni standart holatga keltirish (masalan, kichik harflar)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, password=None, **extra_fields):  # email bu yerga ham qo'shildi
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True, validators=[phone_regex], null=True)
    email = models.EmailField(max_length=255, unique=True, null=True)

    first_name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)


    data_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']  # Mana shu yerda gmail so'raladi
    def __str__(self):
        return self.phone_number