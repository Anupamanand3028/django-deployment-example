from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExUser(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank = True)

    def __self__(self):
        return self.user.username
