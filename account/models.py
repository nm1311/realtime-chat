from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# create a user
# create a superuser

# My custom account manager
class MyAccountManager(BaseUserManager):
    
    # override create_user function 
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email is a required field")
        if not username:
            raise ValueError("Username is a required field")

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )

        user.sert_password(password)
        user.save(self._db)

        return user

    # override create_superusr function 
    def create_superuser(self, email, username, password=None):
        user = create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(self._db)

        return user




def get_default_profile_image(self):
    return "my-chat-application-images/logo_1080_1080.png"

def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/profile_image.png'


# My custom User class
class Account(AbstractBaseUser):
    email               = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    date_joined         = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="Last Login",  auto_now=True)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    profile_image       = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    hide_email          = models.BooleanField(default=True)

    # Tie the custom user to the custom account manager
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    def get_profile_image_filename(self):
        # It takes the file name of the profile image uploaded by the user and changes 
        # it to profile_image.png.
        # ????get back to it
        return str(self.profile_image) [ str(self.profile_image).index(f'profile_images/{self.pk}/') :]