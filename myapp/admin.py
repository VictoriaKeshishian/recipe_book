from django.contrib import admin
from .models import Categories, Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cooking', 'time_cooking', 'img',
                    'author', 'ingredients')
    search_fields = ('name', 'ingredients')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'keywords')








