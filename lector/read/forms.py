from django import forms
from task import tarea
from read.models import Archivo


class FormArchivo(forms.ModelForm):
    class Meta:
        model=Archivo
        fields=('file',)

    def save(self, commit=True):
        file = super(FormArchivo, self).save()
        tarea.delay(file.id)
        return file
