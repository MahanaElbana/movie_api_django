from django.db import models
from django.core.validators import MaxValueValidator ,MinValueValidator
from django.contrib.auth.models import User
#https://pypi.org/project/httpie-django-auth/        
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class StreamPlatform(models.Model):
    name =models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

class WatchList(models.Model):
    #film name
    avarage_rating = models.FloatField(default=0) 
    number_rating = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    #published or not 
    active =models.BooleanField(default=True)
    created =models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform ,on_delete =models.CASCADE,related_name="watchList" )
      
    def __str__(self):
        return self.title

class Review(models.Model):
    user_review =models.ForeignKey(User ,on_delete=models.CASCADE ,related_name="review_user")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200)
    created =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active =models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList ,on_delete=models.CASCADE ,related_name="reviews")

    def __str__(self):
        return str(self.rating)+' | '+self.watchlist.title









#---- second method for create token ----#
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)        
#---- second method for create token ----#        