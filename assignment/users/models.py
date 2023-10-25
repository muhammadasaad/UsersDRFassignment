from django.db import models
from django.core.exceptions import ValidationError
import re

def isusername(name):
    if not re.match(r'^[A-Za-z0-9_.]+$', name):
        raise ValidationError(f'{name} is not a valid username',params={'username':name})
    
def isphone(phone):
    if not re.match(r'^[+]?92[ ]?\d{3}[ ]?\d{7}$',phone): #+92 333 5551234 923335551234 +92 3335551234 all valid
        raise ValidationError(f'{phone} is not a valid phone number',params={'phone':phone})

class Users(models.Model):
    username = models.CharField(max_length=75, unique=True, validators=[isusername])
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[isphone])
    address = models.CharField(max_length=150)
    
   