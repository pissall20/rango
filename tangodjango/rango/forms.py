from django import forms
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User


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
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    url = forms.URLField(max_length=256, help_text="Please enter URL of the page")

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data['url']
        if url and not url.startswith('http://'):
            url = 'http://'+url
            cleaned_data['url'] = url
            return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.EmailField(help_text="Please enter a valid email ID.")
    password = forms.CharField(widget=forms.PasswordInput, help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Please enter a valid URL with http:// prefix. Optional.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload. Optional.", required=False)
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')