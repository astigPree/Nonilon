from django.db import models
from django.core.exceptions import ValidationError
import xml.etree.ElementTree as ET
import random
import string

def validate_svg(file):
    try:
        ET.parse(file)
    except ET.ParseError:
        raise ValidationError("File is not a valid SVG")

def generate_client_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 15)))
    while Client.objects.filter(client_code = code).exists():
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 15)))
    return code

# Create your models here.

class ProgrammingLanguage(models.Model):

    name = models.CharField(max_length=20)
    rating = models.IntegerField(default=50)
    icon =  models.FileField(upload_to='images/', validators=[validate_svg])
    link = models.TextField(default="")

    def __str__(self):
        return self.name


class OtherLanguage(models.Model):

    name = models.CharField(max_length=20)
    rating = models.IntegerField(default=50)
    icon =  models.FileField(upload_to='images/', validators=[validate_svg])
    link = models.TextField(default="")
    def __str__(self):
        return self.name


class UsedFrameWork(models.Model):

    name = models.CharField(max_length=20)
    rating = models.IntegerField(default=50)
    icon =  models.FileField(upload_to='images/', validators=[validate_svg])
    link = models.TextField(default="")
    def __str__(self):
        return self.name
    
    
class UsedLibrary(models.Model):

    name = models.CharField(max_length=20)
    rating = models.IntegerField(default=50)
    icon =  models.FileField(upload_to='images/', validators=[validate_svg])
    link = models.TextField(default="")
    def __str__(self):
        return self.name
    
        
class UsedSoftware(models.Model):

    name = models.CharField(max_length=20)
    rating = models.IntegerField(default=50)
    icon =  models.FileField(upload_to='images/', validators=[validate_svg])
    link = models.TextField(default="")

    def __str__(self):
        return self.name
    
    
class SoftwareProject(models.Model):
    
    name = models.CharField(max_length=225)
    description = models.TextField()
    link = models.TextField(default="#")
    image = models.ImageField(upload_to='images/')
    
    def __str__(self) -> str:
        return self.name
    
    
class HardwareProject(models.Model):
    
    name = models.CharField(max_length=225)
    description = models.TextField()
    link = models.TextField(default="#")
    image = models.ImageField(upload_to='images/')
    
    def __str__(self) -> str:
        return self.name
    

class Client(models.Model):

    client_code = models.CharField(max_length=15, default=generate_client_code)
    name = models.CharField(max_length=15, default="Your Name")
    testimony = models.TextField(max_length=335, default="Write your testimony here")
    rating = models.SmallIntegerField(default=3 )
    
    is_used = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.client_code}: { self.is_used } : {self.name}'