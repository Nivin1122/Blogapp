# Generated by Django 5.1.1 on 2024-10-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comm',
            field=models.TextField(null=True),
        ),
    ]
