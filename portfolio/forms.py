from django.forms import ModelForm, TextInput, Textarea, FileInput, Select

from .models import *


class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'body', 'category', 'tags', 'img', 'zip_file']
        widgets = {'category': Select(attrs={
            "name": "category",
            "id": "category",
            "data-placeholder": "Subject",
            "class": "chosen-select sel-dec",
        }),

            'tags': TextInput(attrs={
                'id': 'id_tags',
                "class": "sd-select",
            })}
