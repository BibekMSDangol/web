from urllib import request
from django import forms
from guitar.models import Guitar

class GuitarForm(forms.ModelForm):

    class Meta:
        model = Guitar
        fields = "__all__"
