# Generated by Django 2.2.20 on 2022-01-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0012_auto_20211116_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseasecase',
            name='doi',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
