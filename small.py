from django.http import HttpResponse
from django.urls import path

DEBUG = True
SECRET_KEY = 'thismustbesecure'
ROOT_URLCONF = __name__

def index(request):
    return HttpResponse('<p>A really small Django project</p>')

urlpatterns = [
    path('', index),
]
