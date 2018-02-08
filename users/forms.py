from django import forms


class UploadFileForm(forms.Form):
    uid = forms.IntegerField()
    file = forms.FileField()
