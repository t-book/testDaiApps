# Generated by Django 2.2.20 on 2021-07-20 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0008_diseasecase_geoserver_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseasecase',
            name='geoserver_id',
        ),
    ]