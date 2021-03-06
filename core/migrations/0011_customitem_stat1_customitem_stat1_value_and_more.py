# Generated by Django 4.0.5 on 2022-06-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_delete_originalitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='customitem',
            name='stat1',
            field=models.CharField(choices=[], default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='customitem',
            name='stat1_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customitem',
            name='stat2',
            field=models.CharField(blank=True, choices=[], default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='customitem',
            name='stat2_value',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customitem',
            name='stat3',
            field=models.CharField(blank=True, choices=[], default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='customitem',
            name='stat3_value',
            field=models.IntegerField(blank=True, default=2),
            preserve_default=False,
        ),
    ]
