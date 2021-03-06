# Generated by Django 4.0.1 on 2022-01-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cjenovnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('kategorija1_cijena', models.DecimalField(decimal_places=2, max_digits=4)),
                ('kategorija2_cijena', models.DecimalField(decimal_places=2, max_digits=4)),
                ('kategorija3_cijena', models.DecimalField(decimal_places=2, max_digits=4)),
                ('kategorija1_granica', models.IntegerField()),
                ('kategorija2_granica', models.IntegerField()),
            ],
        ),
    ]
