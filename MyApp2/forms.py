from django import forms

from .models import norm

class addnewform(forms.ModelForm):

    class Meta:

        model = norm

        fields = ('Name', 'Email', 'Age')
