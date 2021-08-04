from django.db.models import expressions
from django.http import request
from django.shortcuts import redirect, render
from . models import Movies
from . forms import MoviesForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.contrib import messages


# Create your views here.

def index(request):
    pelis = Movies.objects.all()
    return render(request, "principal/index.html",{
        "peliculas": pelis
    })

def addMovie(request):
    if request.method =='GET':
        form = MoviesForm()
        context = {
            'form': form
        }
    else:
        form = MoviesForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added!")
            return redirect('index') #Si es valido que me redireccione al index mostrando el dato ingresado
        
    return render(request, "principal/addMovies.html", context)

def editTitle(request, id):
    movie = Movies.objects.get(id = id)
    if request.method == 'GET':
        form = MoviesForm(instance = movie)
        context = {
            'form': form
        }
    else:
        form = MoviesForm(request.POST, instance = movie)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited!")
            return redirect('index')
    return render(request, "principal/addMovies.html", context)

def deleteMovie (request, id):
    movie = Movies.objects.get(id = id)
    movie.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect('index')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "principal/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, "seba@gmail.com", password)
            user.save()
        except IntegrityError:
            return render(request, "principal/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "principal/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Nice to see you again!")
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "principal/login.html",{
            messages.error(request, "Try again.")             
            })
    else:
        return render(request, "principal/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
