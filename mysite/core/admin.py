from django.contrib import admin

# Register your models here.
from .models import Apps
from .models import media_training
from .models import media_training_video
admin.site.register(Apps)
admin.site.register(media_training)
admin.site.register(media_training_video)