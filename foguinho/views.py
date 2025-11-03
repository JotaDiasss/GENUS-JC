from django.utils import timezone
from datetime import timedelta
from .models import ArvoreAcesso

def atualizar_sequencia_login(usuario):
    arvore, _ = ArvoreAcesso.objects.get_or_create(usuario=usuario)
    hoje = timezone.now().date()
    ontem = hoje - timedelta(days=1)

    if arvore.ultimo_acesso not in [ontem, hoje]:
        arvore.sequencia_atual = 0
        arvore.save()

def registrar_leitura_noticia(usuario):
    if not usuario.is_authenticated:
        return

    hoje = timezone.now().date()
    arvore, created = ArvoreAcesso.objects.get_or_create(usuario=usuario)

    if arvore.ultimo_acesso == hoje:
        pass
    elif arvore.ultimo_acesso == hoje - timedelta(days=1):
        arvore.sequencia_atual += 1
    else:
        arvore.sequencia_atual = 1

    arvore.ultimo_acesso = hoje
    arvore.save()