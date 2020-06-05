from django import forms


class BlogForm(forms.Form):
    name = forms.CharField(max_length=100, label='Blog Name')
    tagline = forms.CharField(widget=forms.Textarea)
    topic = forms.CharField(max_length=200, label='Tema del Blog')
