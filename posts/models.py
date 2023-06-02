from django.db import models
from cloudinary.models import CloudinaryField

#make migrations informs django so that chages reflect in backend

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name =  models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body =  models.CharField(
    'Body', blank=True, null=True, max_length=148, db_index=True
    )
    created_at = models.DateTimeField(
    'Created DateTime', blank=True, auto_now_add=True
    )
    image = CloudinaryField(
        "image", blank = True
    )
    like = models.IntegerField(
       "like" , default= 0, blank=True
    )