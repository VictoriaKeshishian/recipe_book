from django.urls import path
from .views import home, recipe_add, registration_view, login_view, logout_view, recipe_detail, UserProfileView
from .views import user_recipes, edit_recipe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('recipe/add/', recipe_add, name='recipe_add'),
    path('recipe/detail/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('user/recipes/', user_recipes, name='user_recipes'),
    path('recipe/edit/<int:recipe_id>/', edit_recipe, name='edit_recipe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)