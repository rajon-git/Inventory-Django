from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
STATUS_CHOICES = [
    ('INA', 'Inactive'),
    ('A', 'Active'),
    ('OL', 'On_leave')
]

ROLE_CHOICES = [
    ('OP', 'Operative'),
    ('EX', 'Executive'),
    ('AD', 'Admin')
]
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True, verbose_name=('Account ID'), populate_from='email')
    profile_picture  = ProcessedImageField(default='profile_pics/default.jpg', upload_to='profile_pics', format='JPEG',
                                processors = [ResizeToFill(150,150)],
                                options={ 'quality': 100})
    telephone = PhoneNumberField(null=True,blank=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=12, blank=False, null=False, default='INA')
    role = models.CharField(choices=ROLE_CHOICES, max_length=12, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url= self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        ordering = ["slug"]