# Generated by Django 4.2.7 on 2023-11-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_autor_bilhete_director_sessao_alter_cinema_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartaz',
            name='filme',
            field=models.ManyToManyField(blank=True, null=True, to='cinema.filme'),
        ),
    ]
