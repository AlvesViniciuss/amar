# Generated by Django 3.2.20 on 2023-07-22 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20230721_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='senha',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='usuario',
        ),
    ]
