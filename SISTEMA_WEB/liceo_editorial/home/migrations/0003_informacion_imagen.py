# Generated by Django 5.0.2 on 2024-02-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_lgc_remove_informacion_lgc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='informacion_imagenes/'),
        ),
    ]
