from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .forms import CharacterForm
from .models import Character


class CharacterViews(ListView):
    template_name = 'home.html'
    model = Character
    context_object_name = 'characters'


class OwnerCharactersViews(ListView):
    template_name = 'my_char.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return Character.objects.filter(owner=self.request.user)


class CreateCharacter(CreateView):
    form_class = CharacterForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

    model = Character

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ShowCharacter(DetailView):
    model = Character
    template_name = 'char.html'
    context_object_name = 'char'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class CharacterDeleteView(DeleteView):
    model = Character
    success_url = reverse_lazy("home")
    context_object_name = 'char'
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class CharacterUpdateView(UpdateView):
    model = Character
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy("home")


def list_app(request):
    return render(request, 'vuejs_render/list.html')

def create_app(request):
    return render(request, 'vuejs_render/create.html')