from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import random
from django.shortcuts import get_object_or_404


def home(request):

    all_recipes = Recipe.objects.all()
    random_recipes = random.sample(list(all_recipes), min(5, len(all_recipes)))
    context = {'recipes': random_recipes}
    return render(request, 'myapp/home.html', context)


def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'myapp/recipe_add.html', {'form': form})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    cooking_steps = recipe.cooking.split('\n')
    return render(request, 'myapp/recipe_detail.html', {'recipe': recipe, 'cooking_steps': cooking_steps})


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def user_recipes(request):
    user = request.user
    user_recipes = Recipe.objects.filter(author=user)
    context = {'user_recipes': user_recipes}
    return render(request, 'myapp/user_recipes.html', context)


class UserProfileView(TemplateView):
    template_name = 'myapp/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'myapp/recipe_edit.html', {'form': form, 'recipe': recipe})