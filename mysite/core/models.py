from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Apps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    path = models.ImageField()
    pub_create = models.DateTimeField('date de création')
    
    def __str__(self):
        return self.title


class media_training(models.Model):
    app = models.ForeignKey(Apps, on_delete=models.CASCADE)
    title_of_media = models.CharField(default="", max_length=200)
    instruction = models.CharField(max_length=2000, default="")
    url_image = models.ImageField(null=True)
    pub_create = models.DateTimeField('date de création')
    def __str__(self):
        return self.title_of_media

class media_training_video(models.Model):
    app = models.ForeignKey(Apps, on_delete=models.CASCADE)
    title_of_media = models.CharField(default="", max_length=200)
    instruction = models.CharField(max_length=2000, default="")    
    videofile = models.FileField(null=True)
    pub_create = models.DateTimeField('date de création')
    
    def __str__(self):
        return self.title_of_media
