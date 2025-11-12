# Em jornal/urls.py
from django.urls import path
from . import views 

app_name = 'jornal'

urlpatterns = [

    path('noticia/<slug:slug>/', views.pagina_noticias, name='pagina_noticias'),
    path('configuracoes/', views.configuracoes_conta, name='configuracoes_conta'), 
    path('register/', views.register, name='register'),
    
    path('favoritos/', views.ver_favoritos, name='favoritos'), 
    path('favorito/toggle/<int:noticia_id>/', views.toggle_favorito, name='toggle_favorito'),

    path('filtrar/', views.filtrar_por_genero, name='filtrar_por_genero'),

    path('adicionar-noticia/', views.add_aos_fav, name="add"),
    path('favoritos/adicionar/<int:noticia_id>/', views.add_aos_fav, name='add_aos_fav'),
    path('favoritos/remover/<int:noticia_id>/', views.remover_dos_favoritos, name='remover_dos_favoritos'),
    
    path('', views.index, name='index'),
    
    # --- NOVAS URLS PARA O ADMIN SECRETO ---
    path('admin-secreto/', views.admin_secreto_lista, name='admin_secreto_lista'),
    path('admin-secreto/criar/', views.admin_secreto_criar, name='admin_secreto_criar'),
    path('admin-secreto/editar/<int:noticia_id>/', views.admin_secreto_editar, name='admin_secreto_editar'),
    path('admin-secreto/apagar/<int:noticia_id>/', views.admin_secreto_apagar, name='admin_secreto_apagar'),

    # --- ADIÇÃO DESTA NOVA URL ---
    path('admin-secreto/popular-generos/', views.admin_secreto_popular_generos, name='admin_secreto_popular_generos'),
]