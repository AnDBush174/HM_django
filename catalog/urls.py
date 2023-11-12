from django.contrib.messages import success
from django.urls import path
from . import views
from .views import home_view, contacts

urlpatterns = [
    path('', home_view),
    path('', contacts),
    path('', success),
]
