# Generated by Django 4.1.3 on 2022-12-02 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['book'], 'verbose_name': 'Favorite', 'verbose_name_plural': 'Favorites'},
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='isComplit',
            new_name='isComplete',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='isFavorit',
            new_name='isFavorite',
        ),
    ]