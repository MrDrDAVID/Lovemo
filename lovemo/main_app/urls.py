from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('<int:id>/', views.transaction, name='transaction'),
    path('about/', views.about, name='about'),
]
