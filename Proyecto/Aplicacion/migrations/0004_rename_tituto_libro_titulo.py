# Generated by Django 5.0.6 on 2024-09-04 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0003_remove_libro_isbn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='tituto',
            new_name='titulo',
        ),
    ]
