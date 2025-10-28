from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Noticia(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    resumo = models.TextField(null=False)
    detalhes = models.TextField(null=False)
    data = models.DateTimeField("Postado em: ")
    reporter = models.CharField(max_length=200, null=False)
    genero = models.IntegerField(default=0) #a ideia eh que cada genero de noticia represente um numero
    #exemplo politica = 0, esportes = 1, globo = 2, cultura pop = 3. E a gnt faria o algoritimo com base nisso
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} : [{self.resumo}]"
    
    def strcompleta(self):
        return f"{self.titulo} feito por: {self.reporter} no dia {self.data}"
    
    def recente(self):
        return self.data >= timezone.now() - datetime.timedelta(days=1)
    
    def noticia(self):
        return f"{self.detalhes}"
    

class Comentarios(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    texto = models.TextField(null=False)
    likes = models.IntegerField(default=0)
    data = models.DateTimeField("Postado em: ")
    usuario = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"[{self.noticia}] : {self.texto}"

class Favoritos(models.Model):  
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.noticia.titulo}'

# Create your models here.
