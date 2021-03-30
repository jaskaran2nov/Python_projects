from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('titel', 'author','description','code')
        widgets={
            'titel':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'code':forms.Textarea(attrs={'class':'form-control'})
        }