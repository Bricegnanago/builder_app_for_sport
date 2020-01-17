from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Apps
from . models import media_training
from . models import media_training_video

from django.views.generic import TemplateView
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home(request):
    count_user = User.objects.count()
    count_apps = Apps.objects.count()
    apps = Apps.objects.all()

    return render(request, 'home.html', {
        'count_user' : count_user, 
        'count_apps': count_apps,
        'apps': apps
    }
)

@login_required
def entrainements(request, apps_id):
    app = get_object_or_404(Apps, pk=apps_id)
    all_media = media_training.objects.all()
    all_media_video = media_training_video.objects.all()
    medias = []
    media_videos = []
    for media in all_media:
        if media.app.id == apps_id:
            medias.append(media)            

    for media_video in all_media_video:
        if media_video.app.id == apps_id:
            media_videos.append(media_video)

    return render(request,'entrainements.html', 
    {
        'app':app,
        'medias': medias,
        'media_videos': media_videos,
        'count_media' : len(medias),
        'count_media_video': len(media_videos)
    })    

def signup(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html',{'form': form})

# @login_required
# def secret_page(request):
#     return render(request, 'secret_page.html');

# class SecretPage(LoginRequiredMixin, TemplateView):
#     template_name = 'secret_page.html'