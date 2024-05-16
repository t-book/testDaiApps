# Generated by Django 2.2.28 on 2024-02-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daard_database', '0046_auto_20240206_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasecase',
            name='age_class',
            field=models.CharField(choices=[('Fetus (until birth)', 'Fetus (until birth)'), ('Infans (0 – 3\xa0years)', 'Infans (0 – 3\xa0years)'), ('Infans (4 – 6\xa0years)', 'Infans (4 – 6\xa0years)'), ('Infans (7 – 12\xa0years)', 'Infans (7 – 12\xa0years)'), ('Adolescent (13 – 20\xa0years)', 'Adolescent (13 – 20\xa0years)'), ('Early Adult (21 – 35\xa0years)', 'Early Adult (21 – 35\xa0years)'), ('Late Adult (36 – 50\xa0years)', 'Late Adult (36 – 50\xa0years)'), ('Senile (50 +\xa0years)', 'Senile (50 +\xa0years)'), ('Adult', 'Adult'), ('Non-Adult', 'Non-Adult'), ('unknown', 'unknown')], max_length=200),
        ),
        migrations.AlterField(
            model_name='diseasecase',
            name='sex',
            field=models.CharField(choices=[('f', 'F'), ('f?', 'F?'), ('unknown', 'unknown'), ('m', 'M'), ('m?', 'M?')], max_length=200),
        ),
    ]