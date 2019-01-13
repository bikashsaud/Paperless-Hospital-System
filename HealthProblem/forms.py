from django.forms import ModelForm
from django import forms
from UserComment.models import Comment
class CommentForm(forms.ModelForm):
    email=forms.CharField(label='Email',widget=forms.EmailInput(attrs={"class":'form-control'}))
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={"class":'form-control'}))
    phoneno=forms.CharField(label='Phone No',widget=forms.TextInput(attrs={"class":'form-control'}))
    comment=forms.CharField(label='Comment',widget=forms.TextInput(attrs={"class":'form-control'}))

    class Meta:
        model=Comment
        fields='__all__'
