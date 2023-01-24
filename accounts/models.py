import imp
from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from PIL import Image
from django.core.validators import MinValueValidator,FileExtensionValidator
from .validators import validate_file_size

""" USER OBJECTS MANAGER """
class UserManager(BaseUserManager):

    """ CREATING USER """
    def create_user(self, name,username,email,password=None):

        """ USER VALIDATORS """
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        if not name:
            raise ValueError('User must have a name')    

        """ SAVING USER TO DB """
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            name = name,            
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            name = name,           
            
            )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        
        user.save(using=self._db)
        return user



""" USER MODELS """
class User(AbstractUser):
    """ USER NAME AND EMAIL """
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(max_length=150, unique=True)

    """ USER BOOL FIELDS """

    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=False)
    is_superadmin       = models.BooleanField(default=False)

    """ USER DATES """

    date_joined         = models.DateTimeField(auto_now_add=True)
    last_login          = models.DateTimeField(auto_now=True)

    """ USER LOGIN DETAILS """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    """ USER MANAGER """
    objects = UserManager()


    """ USER PARAMS """
    def full_name(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


""" USER PROFILE IMAGE """
class Profile(models.Model):
    user                = models.OneToOneField(User,on_delete=models.CASCADE)         
    image = models.ImageField(default='logo-whitebg.jpg',upload_to = "accounts/user/profile",validators=[validate_file_size, FileExtensionValidator(allowed_extensions=['png','jpg'])])                  
    phoneNumber = models.CharField(max_length=50,blank=True,null=True)
    phoneID = models.CharField(max_length=50,blank=True,null=True)
    date_created        = models.DateTimeField(auto_now_add=True)
    date_updated        = models.DateTimeField(auto_now=True)

   
    @property
    def email(self):
        return "%s"%(self.user.email)


    @property
    def full_name(self):
        return "%s"%f'{self.user.name} - {self.user.email}'


    def __str__(self):
        return f'{self.user.name} - {self.user.email}'
    
  
        