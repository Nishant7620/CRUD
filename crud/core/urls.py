from django.urls import path
from core import views

urlpatterns = [
    path('home/',views.home),
    path('delete /<int:id>/',views.delete, name = 'delete')
]
