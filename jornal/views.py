from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia, Favoritos, Genero, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def lista_de_noticias(request):
    noticias = Noticia.objects.all().order_by('-data')
    return render(request, 'index.html', { 'noticias': noticias})

def pagina_noticias(request, slug):
    noticia = Noticia.objects.get(slug=slug)
    return render(request, 'pagina-noticia.html', { 'noticia': noticia})

def index(request):
    query = request.GET.get('q') 
    if query:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains=query) |
            Q(resumo__icontains=query) |
            Q(detalhes__icontains=query)
        ).distinct().order_by('-data')
    else:
        noticias = Noticia.objects.all().order_by('-data')[:8]
    contexto = {
        'noticias': noticias,
        'query': query,
    }
    return render(request, 'index.html', contexto)

@login_required
def ver_favoritos(request):
    favoritos_itens = Favoritos.objects.filter(usuario=request.user).order_by('-adicionado')
    noticias_favoritas = [item.noticia for item in favoritos_itens]
    context = {
        'favoritos': noticias_favoritas
    }
    return render(request, 'favoritos.html', context)

@login_required
def add_aos_fav(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if not Favoritos.objects.filter(usuario=request.user, noticia=noticia).exists():
        Favoritos.objects.create(usuario=request.user, noticia=noticia)
    return redirect('jornal:index')

@login_required
def remover_dos_favoritos(request, noticia_id):
    if request.method == 'POST':
        noticia = get_object_or_404(Noticia, id=noticia_id)
        try:
            favoritos_itens = Favoritos.objects.get(usuario=request.user, noticia=noticia)
            favoritos_itens.delete()
        except Favoritos.DoesNotExist:
            pass 

    return redirect('jornal:favoritos')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'registration/register.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Este email já está cadastrado.')
            return render(request, 'registration/register.html')
        
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        
        login(request, user)
        return redirect('jornal:index')
    
    return render(request, 'registration/register.html')


@login_required
def configuracoes_conta(request):
    profile = request.user.profile
    
    if request.method == 'POST':
        generos_selecionados_nomes = request.POST.getlist('genres')
        generos_objs = Genero.objects.filter(nome__in=generos_selecionados_nomes)
        profile.generos_favoritos.set(generos_objs)
        return redirect('jornal:configuracoes_conta')

    all_genres = Genero.objects.all()
    generos_salvos = profile.generos_favoritos.all()
    
    context = {
        'all_genres': all_genres,
        'generos_salvos': generos_salvos
    }
    return render(request, 'configuracoes.html', context)