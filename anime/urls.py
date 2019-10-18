from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index_list, name='index_list'),
    path('index/anime_list', views.anime_list, name='anime_list'),
    path('index/galeria_list', views.galeria_list, name='galeria_list'),
    path('index/manga_list', views.manga_list, name='manga_list'),
    path('index/nosotros_list', views.nosotros_list, name='nosotros_list'),
    path('index/objeto_list', views.objeto_list, name='objeto_list'),
    path('index/registro_list', views.registro_list, name='registro_list'),
]