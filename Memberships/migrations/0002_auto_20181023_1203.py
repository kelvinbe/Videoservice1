# Generated by Django 2.1.2 on 2018-10-23 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Memberships', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='Membership_type',
            new_name='membership_type',
        ),
    ]
