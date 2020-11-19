# Generated by Django 3.0.7 on 2020-11-13 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0032_remove_statement_prototype'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='prototype',
            field=models.ForeignKey(blank=True, help_text='Prototype statement', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instances', to='controls.Statement'),
        ),
    ]
