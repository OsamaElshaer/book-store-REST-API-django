# Generated by Django 4.1.3 on 2022-12-15 22:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_alter_favorite_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Payment',
        ),
    ]
