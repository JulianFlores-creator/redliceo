# Generated by Django 5.0.2 on 2024-02-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorias_red_liceo', '0002_alter_documentomemoria_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentomemoria',
            name='documento',
            field=models.FileField(upload_to='memorias_red_liceo/encuentros/'),
        ),
    ]
