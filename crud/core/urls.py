from django.urls import path
from core import views

urlpatterns = [
    path('home/',views.home),
    path('update/<int:id>/',views.update,),
    path('delete/<int:id>/',views.delete, name = 'delete')
]
