from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('update_tf/<str:pk>/', views.updateTarefa, name='update'),
    path('delete_tf/<str:pk>/', views.deleteTarefa, name='delete')

]