# Generated by Django 2.2.16 on 2022-07-21 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20220721_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title_id',
            new_name='title',
        ),
    ]
