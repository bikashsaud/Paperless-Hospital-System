from django.forms import ModelForm
from django import forms
from UserComment.models import Comment
class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields='__all__'
