from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import RequestContext
from django.urls import reverse
from .forms import ChampionForm, ItemForm, NameForm, CreateChampionForm
from .models import CustomChampion, CustomItem

def index_view(request):
    return render(request, 'core/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            id = request.user.id
            name = request.user.username
            return redirect('/profile')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', { 'form': form })
            
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

# def get_name(request):
#     if request.method == 'POST':
#         # form = NameForm(request.POST)
#         form = CreateChampionForm(request.POST)
#         if form.is_valid():
#             return redirect('/profile')
#     else:
#         form = CreateChampionForm()

#     return render(request, 'core/create.html', {'form': form })

# def crispy_view(request):
#     form = CreateChampionForm(request.POST)
#     return render(request, 'core/crispy.html', {'form': form})

def create(request):
    return render(request, 'core/create.html')

# VIEW WITH MODEL TO FORM
def create_champion(request):
    if request.method == 'POST':
        print("Method POST requested")
        form = ChampionForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            redirect('/')
    
        if not form.is_valid():
            print("Form is not valid")
            messages.error(request, "Form is not valid")
            print(form.errors)
            return render(request, 'core/create.html', context={'form': form})
    else:
        form = ChampionForm()
        print("Something went wrong")
    
    context = {"form": form}
    # redirect('/')
    return render(request, 'core/create_champion.html', context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
        if not form.is_valid():
            messages.error(request, "Form is not valid")
            print(form.errors)
            return render(request, 'core/create_item.html', context={'form': form})
    else:
        form = ItemForm()
    
    context = {"form": form}
    return render(request, 'core/create_item.html', context)

def list(request):
    return render(request, 'core/list.html')

def list_champions(request):
    champions = CustomChampion.objects.all()
    return render(request, 'core/list_champions.html', {'champions': champions})

def list_items(request):
    items = CustomItem.objects.all()
    return render(request, 'core/list_items.html', {'items': items})

def champion_detail(request, slug):
    champion = get_object_or_404(CustomChampion, slug=slug)
    return render(request, 'core/champion.html', {'champion': champion})

def item_detail(request, slug):
    item = get_object_or_404(CustomItem, slug=slug)
    return render(request, 'core/item.html', {'item': item})