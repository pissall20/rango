from django import forms
from rango.models import Category, Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=250, help_text="Please enter a category")
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    slug = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Category
        fields = ('name', )

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=150, help_text="Please enter the title of the page")
    views = forms.IntegerField(widget=forms.HiddenInput,initial=0)
    url = forms.URLField(max_length=256,help_text="Please enter URL of the page")

    class Meta:
        model = Page
        exclude = ('category',)