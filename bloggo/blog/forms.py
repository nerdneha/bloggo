from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
