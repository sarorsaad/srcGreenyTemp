from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.dispatch import receiver
from django.db.models.signals import post_save

#Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='users', blank=True, null=True)
    code = models.CharField(max_length=10,default=generate_code, unique=True)
    code_used = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

class UserPersonal_info(models.Model):
    user = models.ForeignKey(User,related_name='personal_info' , on_delete=models.CASCADE)
    iqama_id = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=20, unique=True)

class UserBio_info(models.Model):
    user = models.ForeignKey(User,related_name='bio_info' , on_delete=models.CASCADE)
    JOB_POSITION_CHOICES = [
    ('resident', 'Resident'),
    ('specialist', 'Specialist'),
    ('consultant', 'Consultant'),
    ('technician', 'technician'),
    ]
    job_position = models.CharField(max_length=50, choices=JOB_POSITION_CHOICES)
    department = models.CharField(max_length=50)
    SCFHS = models.CharField(max_length=20, unique=True)

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created :
       Profile.objects.create(user=instance)