from django import forms
from django import forms
from home.models import Blog

class Edit_Blog(forms.ModelForm):
    class Meta():
        model = Blog
        fields = '__all__'