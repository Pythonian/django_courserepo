# Generated by Django 4.0.6 on 2022-07-06 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_remove_material_level_material_impressions'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='lecturer',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
