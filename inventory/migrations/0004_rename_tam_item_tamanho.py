# Generated by Django 3.2.20 on 2023-07-22 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20230721_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='tam',
            new_name='tamanho',
        ),
    ]