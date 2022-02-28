# Generated by Django 4.0.2 on 2022-02-27 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0001_initial'),
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.persona'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(to='mascota.Vacuna'),
        ),
    ]
