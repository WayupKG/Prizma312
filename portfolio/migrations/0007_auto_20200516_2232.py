# Generated by Django 3.0.6 on 2020-05-16 16:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio_teg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
    ]