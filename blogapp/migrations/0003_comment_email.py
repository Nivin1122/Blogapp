# Generated by Django 5.1.1 on 2024-10-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_rename_writter_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
