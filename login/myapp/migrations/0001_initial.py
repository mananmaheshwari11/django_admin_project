# Generated by Django 5.0.6 on 2024-06-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=12)),
                ('cfmpwd', models.CharField(max_length=12)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
