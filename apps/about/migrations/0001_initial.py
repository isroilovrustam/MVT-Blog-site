# Generated by Django 4.2.7 on 2023-11-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=202)),
                ('job', models.CharField(max_length=202)),
                ('image', models.ImageField(upload_to='about/')),
                ('title', models.CharField(max_length=202)),
                ('description', models.TextField()),
                ('twitter', models.CharField(max_length=202)),
                ('facebook', models.CharField(max_length=202)),
                ('instagram', models.CharField(max_length=202)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
