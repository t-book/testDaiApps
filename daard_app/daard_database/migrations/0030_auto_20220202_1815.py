# Generated by Django 2.2.20 on 2022-02-02 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0029_auto_20220202_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diseasecase',
            name='dating_method',
        ),
        migrations.RemoveField(
            model_name='diseasecase',
            name='storage_place',
        ),
    ]
