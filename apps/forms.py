from django import forms

class PostCommentForm(forms.Form):
    text = forms.CharField(max_length=200, required=True)