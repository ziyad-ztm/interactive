# Generated by Django 4.2.1 on 2023-07-22 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
