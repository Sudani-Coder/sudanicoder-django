# Generated by Django 3.0.4 on 2020-04-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Phone',
            field=models.CharField(max_length=13),
        ),
    ]