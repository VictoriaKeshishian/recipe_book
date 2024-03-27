from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking', 'time_cooking', 'img', 'ingredients']

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