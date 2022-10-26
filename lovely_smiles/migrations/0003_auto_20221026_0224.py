# Generated by Django 3.2.15 on 2022-10-26 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovely_smiles', '0002_auto_20221022_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='dentist',
            field=models.CharField(choices=[('Dr_Becket', 'Dr. Becket'), ('Dr_Giku', 'Dr. Giku')], default='Dr_Becket', max_length=25),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('Consultation', 'Consultation'), ('Bridges', 'Bridges'), ('Crowns', 'Crowns'), ('Fillings', 'Fillings'), ('Canal', 'Root canal treatment'), ('Scale', 'Scale and polish'), ('Braces', 'Braces'), ('Wisdom', 'Wisdom tooth removal'), ('Implants', 'Dental implants'), ('Dentures', 'Dentures or false teeth'), ('Whitening', 'Teeth whitening'), ('Veneers', 'Dental veneers')], default='Consultation', max_length=25),
        ),
    ]
