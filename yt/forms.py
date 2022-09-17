from django import forms

class Downloads(forms.Form):
    link = forms.URLField()

    