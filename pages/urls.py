
from django.urls import path
from .views import homePageView
# Create your models here.

urlpatterns = [
    path('', homePageView, name='home'),
]