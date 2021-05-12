from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

posts = [
    {
        'author': 'Eldzej02',
        'title': 'Birthday',
        'content': 'A birthday is the anniversary of the birth of a person, or figuratively of an institution. Birthdays of people are celebrated in numerous cultures, often with birthday gifts, birthday cards, a birthday party, or a rite of passage.',
        'date': '10 May 2021',
    },
    {
        'author': 'Eldzej02',
        'title': 'Previous day',
        'content': 'I didn\'t feel well the previous day, i must say.',
        'date': '11 May 2021',
    },
    {
        'author': 'Eldzej02',
        'title': 'Today\'s day',
        'content': 'Today was sunny at the morning but later, during the noon it started raining',
        'date': '12 May 2021',
    }
]

def index(request):
    context = {}
    if request.user.is_authenticated:
        context['parent_template'] = 'home.html'
        context['posts'] = posts
    else:
        context['parent_template'] = 'index_not_auth.html'
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'register.html', {'form':form})