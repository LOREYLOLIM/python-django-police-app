from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report, name='report'),
    path('police', views.police, name='police'),
    path('police/delete/<int:id>', views.delete, name='delete_police')
]