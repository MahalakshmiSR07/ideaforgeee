from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'domain', 'technology', 'difficulty', 'estimated_time', 'learning_resources', 'roadmap']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'learning_resources': forms.Textarea(attrs={'rows': 3}),
            'roadmap': forms.Textarea(attrs={'rows': 4}),
        }
