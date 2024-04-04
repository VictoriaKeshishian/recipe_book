from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .models import Recipe, Categories
from .forms import RecipeForm, UserChangeNameForm, RecipeSearchForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import random
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.db.models.functions import Lower


def home(request):
    all_recipes = Recipe.objects.all()
    random_recipes = random.sample(list(all_recipes), min(6, len(all_recipes)))
    context = {'recipes': random_recipes}
    return render(request, 'myapp/home.html', context)


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


class MyLoginView(LoginView):
    template_name = 'myapp/login.html'


class MyLogoutView(LogoutView):
    template_name = 'myapp/logout.html'
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.get(request, *args, **kwargs)
        else:
            return super().dispatch(request, *args, **kwargs)


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


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'myapp/password_change.html'
    success_url = reverse_lazy('password_change_done')  # URL, на который будет перенаправлен пользователь после успешного изменения пароля

    def form_valid(self, form):
        messages.success(self.request, 'Пароль успешно изменен.')  # Выводим сообщение об успешном изменении пароля
        return super().form_valid(form)


class MyPasswordChangeDoneView(TemplateView):
    template_name = 'myapp/done.html'


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user == recipe.author:
        recipe.delete()
        messages.success(request, "Рецепт успешно удален.")
    else:
        messages.error(request, "Вы не являетесь автором этого рецепта и не можете его удалить.")
    return redirect('user_recipes')


def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'myapp/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = Categories.objects.get(pk=category_id)
    recipes = category.recipes.all()
    return render(request, 'myapp/category_detail.html', {'category': category, 'recipes': recipes})


def change_username(request):
    if request.method == 'POST':
        form = UserChangeNameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserChangeNameForm(instance=request.user)
    return render(request, 'myapp/change_username.html', {'form': form})


@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, "Рецепт успешно добавлен.")
            return redirect('home')
        else:
            messages.error(request, "Пожалуйста, заполните все обязательные поля и добавьте изображение.")
    else:
        form = RecipeForm()

    if not request.user.is_authenticated:
        messages.info(request, "Для добавления рецепта необходимо войти в свой профиль.")

    return render(request, 'myapp/recipe_add.html', {'form': form})


def search_recipes(request):
    search_form = RecipeSearchForm(request.GET)
    search_results = []

    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        all_recipes = Recipe.objects.all()
        for recipe in all_recipes:
            if search_query.lower() in recipe.name.lower():
                search_results.append(recipe)

    return render(request, 'myapp/search_recipes.html', {'search_form': search_form, 'search_results': search_results})
