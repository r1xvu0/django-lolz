# Generated by Django 4.0.5 on 2022-06-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_customitem_stat2_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customitem',
            name='active_stat_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='customitem',
            name='passive_stat_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
