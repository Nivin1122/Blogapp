# Generated by Django 5.1.1 on 2024-09-26 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='writter',
            new_name='title',
        ),
    ]
