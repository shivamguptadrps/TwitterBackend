from django.db import models
from Todobackend.settings import BASE_DIR


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return str(BASE_DIR)+'/listtodo/static/img/{}'.format(filename)


class Tweet(models.Model):
    id =models.IntegerField(primary_key=True)
    desc = models.CharField(max_length=250)
    tweetedby = models.IntegerField()
    tweetedon  = models.IntegerField()
    img = models.ImageField(upload_to='listtodo/static/img' )
    def __str__(self):
        return self.desc
class Users(models.Model):
    id  = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20,unique = True)
    userfullname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    useremail = models.CharField(max_length=50)
    usern_mobile_no = models.CharField(max_length=13)
    profile_pic = models.ImageField(upload_to='listtodo/static/img')
    def __str__(self):
        return self.userfullname
class Following(models.Model):
    id =models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    followedby = models.IntegerField()



























# Create your models here.
