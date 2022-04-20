from django.forms import ModelForm

from app.models import Todos


class ToDoForm(ModelForm):
    class Meta:
        model= Todos
        fields = ['name', 'description', 'finished',]
    
