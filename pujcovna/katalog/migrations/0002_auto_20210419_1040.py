# Generated by Django 3.2 on 2021-04-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaznik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
                ('prijmeni', models.CharField(max_length=100)),
                ('RP_cislo', models.CharField(max_length=20)),
                ('dat_narozeni', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='auto',
            name='najeto_km',
            field=models.IntegerField(),
        ),
    ]
