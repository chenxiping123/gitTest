# Generated by Django 3.2.15 on 2022-08-21 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='Award/')),
            ],
        ),
    ]
