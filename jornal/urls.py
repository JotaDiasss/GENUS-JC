from django.urls import path
from . import views 

app_name = 'jornal'

urlpatterns = [

    path('noticia/<slug:slug>/', views.pagina_noticias, name='pagina_noticias'),
    path('configuracoes/', views.configuracoes_conta, name='configuracoes_conta'), 
    path('register/', views.register, name='register'),
    
    path('favoritos/', views.ver_favoritos, name='favoritos'), 
    
    path('favorito/toggle/<int:noticia_id>/', views.toggle_favorito, name='toggle_favorito'),

    path('adicionar-noticia/', views.add_aos_fav, name="add"),
    path('favoritos/adicionar/<int:noticia_id>/', views.add_aos_fav, name='add_aos_fav'),
    path('favoritos/remover/<int:noticia_id>/', views.remover_dos_favoritos, name='remover_dos_favoritos'),
    
    path('', views.index, name='index'),
    
]