# Generated by Django 4.2.7 on 2023-11-16 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0011_cartaz_molde'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessao',
            name='cinema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.cinema'),
        ),
    ]
