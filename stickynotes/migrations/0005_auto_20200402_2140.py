# Generated by Django 3.0.3 on 2020-04-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickynotes', '0004_auto_20200402_2042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='note',
            name='background_color',
            field=models.CharField(max_length=10),
        ),
    ]
