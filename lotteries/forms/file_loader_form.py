from django import forms

class FileLoaderForm(forms.Form):
    data_file = forms.FileField()