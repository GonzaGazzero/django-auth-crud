# Generated by Django 4.2.4 on 2023-08-14 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_description_task_descripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='importante',
            new_name='important',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='titulo',
            new_name='title',
        ),
    ]
