# Generated by Django 4.2.6 on 2023-10-12 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('name',), 'verbose_name': 'урок', 'verbose_name_plural': 'уроки'},
        ),
    ]
