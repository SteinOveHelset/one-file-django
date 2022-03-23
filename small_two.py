import sys

from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

settings.configure(
    DEBUG=True,
    SECRET_KEY='thismustbesecure',
    ROOT_URLCONF=__name__,
)

def index(request):
    return HttpResponse('<p>A 22 lines Django project</p>')

urlpatterns = [
    path('', index),
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
