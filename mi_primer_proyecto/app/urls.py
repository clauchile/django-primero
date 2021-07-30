from django.urls import path     
from . import views
urlpatterns = [

    path('/', views.root),
    path('blogs/', views.index),
    path('blogs/new/', views.new),
    path('blogs/create/', views.create),
    path('blogs/<int:val>/', views.show),
    path('blogs/<int:number>/edit/', views.edit),
    path('blogs/<int:number>/delete/', views.destroy),
    path('blogs/Json/', views.Json),




    
]
