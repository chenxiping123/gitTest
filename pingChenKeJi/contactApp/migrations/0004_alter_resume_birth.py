# Generated by Django 3.2.15 on 2022-12-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0003_alter_resume_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2022-12-31', max_length=20, verbose_name='出生日期'),
        ),
    ]
