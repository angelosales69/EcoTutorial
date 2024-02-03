from django.forms import ModelForm
from .models import Author, Tutorial


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class TutorialForm(ModelForm):
    class Meta:
        model = Tutorial
        fields = '__all__'
