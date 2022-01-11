# Generated by Django 4.0.1 on 2022-01-10 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mjesta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ulica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulica', models.CharField(max_length=50)),
                ('mjesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mjesta.mjesto')),
            ],
        ),
    ]
