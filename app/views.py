from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Journal,Paper
# Create your views here.

@login_required(login_url='login')
def index(request):
    all_journals = Journal.objects.all()
    return render(request, 'pages/index.html',{'journals':all_journals})


@login_required(login_url='login')
def aim(request):
    return render(request, 'pages/aim.html')

@login_required(login_url='login')
def scope(request):
    return render(request, 'pages/scope.html')

@login_required(login_url='login')
def team(request):
    return render(request, 'pages/team.html')

@login_required(login_url='login')
def privacy(request):
    return render(request, 'pages/privacy.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'pages/contact.html')

@login_required(login_url='login')
def papers(request,journal_id):
    papers = Paper.objects.filter(journal_id=journal_id)
    return render(request, 'pages/papers.html',{'papers':papers})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'pages/register.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate username
        if not username:
            return redirect('register')

        # Validate passwords match
        if password != confirm_password:
            return redirect('register')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return redirect('register')

        if User.objects.filter(email=email).exists():
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print('user created')
        return redirect('login')
    print('user not created')
    return render(request, 'pages/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('index')  # Redirect to a home page or dashboard
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'pages/login.html')


def logout_view(request):
    logout(request)  # Logs the user out
    messages.success(request, "You have been successfully logged out!")
    return redirect('login')  # Redirect to the login page or home page