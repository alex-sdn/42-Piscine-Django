from django import forms


class PublishForm(forms.Form):
    title = forms.CharField(max_length=64)
    synopsis = forms.CharField(max_length=312)
    content = forms.CharField()
