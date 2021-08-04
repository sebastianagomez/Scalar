from django.shortcuts import render, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from . forms import MoviesForm
from . models import Movies
from django.contrib.auth.mixins import LoginRequiredMixin

class MoviesList(ListView):
    model = Movies
    template_name = 'Principal/index.html'

class MoviesCreate(CreateView):
    model = Movies
    form_class = MoviesForm
    template_name = 'Principal/addMovies.html'
    success_url = reverse_lazy('index')

class MoviesUpdate(UpdateView):
    model = Movies
    form_class = MoviesForm
    template_name = 'Principal/updateMovies.html'
    success_url = reverse_lazy('index')

class MovieDetail(DetailView):
    model = Movies
    template_name = 'Principal/detailMovie.html'


