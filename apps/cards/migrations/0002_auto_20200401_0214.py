# Generated by Django 2.2.11 on 2020-04-01 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ('text',)},
        ),
    ]
