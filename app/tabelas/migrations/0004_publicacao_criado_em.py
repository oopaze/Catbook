# Generated by Django 3.1.2 on 2020-12-05 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tabelas', '0003_comentario_like_publicacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacao',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]