from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

# Create your views here.

def home(request):
    return render(request,'sentiment_analyser/home.html')

def form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thanks for registering!')
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'sentiment_analyser/form.html', {'form':form})

def about(request):
    return render(request, 'sentiment_analyser/about.html')

def dashboard(request):
    return render(request, 'sentiment_analyser/dashboard.html')

def dashboard2(request):
    return render(request,'sentiment_analyser/dashboard2.html')
             

