from django import forms
from .models import Recipe, Categories
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking', 'time_cooking', 'img', 'ingredients']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['img'].required = False

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        instance.author = user
        if commit:
            instance.save()
        return instance


class CategoriesForm(forms.Form):
    name = forms.CharField(max_length=100)
    img = forms.ImageField(required=False)
    keywords = forms.CharField(max_length=100)


class UserChangeNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Новое имя пользователя'


class RecipeSearchForm(forms.Form):
    search_query = forms.CharField(label='Поиск', max_length=100)