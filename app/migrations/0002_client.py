# Generated by Django 4.0.4 on 2022-06-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='John55', max_length=30)),
                ('first_name', models.CharField(default='John', max_length=30)),
                ('last_name', models.CharField(default='Doe', max_length=30)),
                ('email', models.EmailField(default='john@gmail.com', max_length=30)),
                ('phone_number', models.IntegerField(null=True)),
            ],
        ),
    ]
