from django import forms
from django.forms import TextInput,Textarea,FileInput
from home.models import Blog,About
from ckeditor.widgets import CKEditorWidget

class Edit_Blog(forms.ModelForm):
    class Meta():
        model = Blog
        fields = '__all__'

class AboutForm(forms.ModelForm):
    Description = forms.CharField(widget=CKEditorWidget())
    class Meta():
        model = About
        fields = ('Title','Description','Image','Url','SMTitle','SMDescription','SMKeywords')

        widgets = {
            'Title': TextInput(attrs={'class' : 'form-control'}),
            'Image' : FileInput(attrs={'class' : 'form-control'}),
            'Description' : Textarea(attrs={'class':'form-control'}),
            'Url' : TextInput(attrs={'class' : 'form-control'}),
            'SMTitle' : TextInput(attrs={'class' : 'form-control'}),
            'SMKeywords' : TextInput(attrs={'class' : 'form-control'}),
            'SMDescription' : Textarea(attrs={'class' : 'form-control'}),
        }