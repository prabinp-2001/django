from app1.models import books
from django.forms import ModelForm

class bookForm(ModelForm):
    class Meta:
        model=books
        fields='__all__'