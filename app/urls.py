from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.list, name='index'),
    path('create', views.create, name='create'),
    path('<id>', views.details, name='details' ),
    path('<id>/update', views.update, name='update' ),
    path('<id>/delete', views.delete, name='delete' ),
]