from django.urls import path
from . import views
from .views import home_view

urlpatterns = [
    path('', home_view),
#    path('contacts/', views.contacts, name='contacts'),
#    path('success/', views.success, name='success'),
]
