from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    users = User.objects.all().order_by("-id")
    
    context = {
        "users": users
    }
    return render(request,"users/index.html",context)

def create(request):
    form_action = reverse("users:create")
    
    #POST
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "O usuário foi cadastrado com sucesso!")
            return redirect("users:index")
        
        context = {
            "form": form,
            "form_action": form_action,
        }
        return render(request,"users/create.html", context)

    #GET
    form = UserForm()
    context = {
        "form": form
    }
    return render(request,"users/create.html", context)

def update(request, username):
    return render(request,"users/create.html")

def delete(request, id):
    user = get_object_or_404(User, id=id)
    
    user.delete()
    return redirect("users:index")
    

def login(request):

    form = AuthenticationForm(request)
    
    #POST
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            
            next = request.POST.get("next")
            
            return redirect(next) if next else redirect("products:index")
            
    #GET        
    context = {
        "form": form
    }
    
    return render(request,"users/login.html", context)

def logout(request):
    auth.logout(request)
    return redirect("users:login")