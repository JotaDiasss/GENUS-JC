from django.contrib import admin
from .models import Noticia, Genero, Comentarios, Favoritos

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'reporter', 'data')
    list_filter = ('generos', 'data', 'reporter')
    search_fields = ('titulo', 'resumo', 'detalhes')
    filter_horizontal = ('generos',)

admin.site.register(Comentarios)
admin.site.register(Favoritos)