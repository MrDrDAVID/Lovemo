from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.transaction, name='transaction'),
    path('about/', views.about, name='about'),
    path('creators', views.creators, name='creators'),
    path('create_transaction/', views.create_transaction, name='create'),
]
