# Generated by Django 5.0.1 on 2024-02-15 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
