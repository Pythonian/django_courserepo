# Generated by Django 4.0.6 on 2022-08-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0006_alter_course_options_alter_material_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]
