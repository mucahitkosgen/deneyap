# Generated by Django 3.0.8 on 2021-05-28 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_siteinfo_phone_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteinfo',
            name='bip',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='copyright',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='footer_address',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='hours_of_service',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='privacy_policy',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='site_url',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='telegram',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='user_agreement',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='youtube',
        ),
    ]