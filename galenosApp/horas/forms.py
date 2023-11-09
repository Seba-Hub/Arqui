from django.forms import ModelForm
from .models import Hora


class HoraForm(ModelForm):
    class Meta:
        model = Hora
        fields = "__all__"
