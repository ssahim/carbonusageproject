# Generated by Django 3.2.8 on 2021-10-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0005_auto_20211013_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usage_type',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
