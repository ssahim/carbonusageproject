# Generated by Django 3.2.8 on 2021-10-19 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0009_alter_usage_user_id'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
