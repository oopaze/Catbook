# Generated by Django 3.1.2 on 2020-12-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabelas', '0005_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]
