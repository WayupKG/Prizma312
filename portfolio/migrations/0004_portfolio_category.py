# Generated by Django 3.0.6 on 2020-05-16 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200516_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='portfolio.Category'),
        ),
    ]
