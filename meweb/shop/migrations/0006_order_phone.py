# Generated by Django 3.1.3 on 2021-01-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=30),
        ),
    ]