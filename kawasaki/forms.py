from django import forms
from kawasaki.models import Kawasaki
class KawasakiForm(forms.ModelForm):
        class Meta:
               model=Kawasaki
               fields="__all__"
