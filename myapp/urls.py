from django.urls import path
from .views import (
    home, recipe_add, registration_view, MyLoginView, MyLogoutView, recipe_detail, UserProfileView,
    user_recipes, edit_recipe, MyPasswordChangeView, MyPasswordChangeDoneView, delete_recipe,
    category_detail, category_list, change_username, search_recipes
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('recipe/add/', recipe_add, name='recipe_add'),
    path('recipe/detail/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('registration/', registration_view, name='registration'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('accounts/profile/', UserProfileView.as_view(), name='user_profile'),
    path('user/recipes/', user_recipes, name='user_recipes'),
    path('recipe/edit/<int:recipe_id>/', edit_recipe, name='edit_recipe'),
    path('password_change/', MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', MyPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('recipe/delete/<int:recipe_id>/', delete_recipe, name='delete_recipe'),
    path('categories/', category_list, name='category_list'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('change_username/', change_username, name='change_username'),
    path('search/', search_recipes, name='search_recipes'),
]

# Добавляем обслуживание медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
