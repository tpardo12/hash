
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('register/', views.add_items, name='add-items'),
    path('check/', views.check, name= 'check'),
    path('check_multiple/', views.checkMultiple, name= 'checkMultiple')
    
]