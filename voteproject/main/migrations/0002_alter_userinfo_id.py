# Generated by Django 4.1.7 on 2023-02-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
