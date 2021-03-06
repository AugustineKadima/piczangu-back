# Generated by Django 4.0.4 on 2022-06-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_client_email_alter_client_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='country',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='region',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='type',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
