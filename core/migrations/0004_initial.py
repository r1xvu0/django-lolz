# Generated by Django 4.0.5 on 2022-06-24 08:45

import autoslug.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_delete_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomChampion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=('name', 'title'), unique=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('controller', 'Controller'), ('fighter', 'Fighter'), ('mage', 'Mage'), ('marksman', 'Marksman'), ('slayer', 'Slayer'), ('tank', 'Tank'), ('specialist', 'Specialist')], default=0, max_length=20)),
                ('lore', models.TextField(blank=True)),
                ('resource', models.CharField(choices=[('mana', 'Mana'), ('health', 'Health'), ('energy', 'Energy'), ('rage', 'Rage'), ('focus', 'Focus'), ('runic_power', 'Runic Power'), ('none', 'None')], default=0, max_length=20)),
                ('base_hp', models.IntegerField()),
                ('base_mp', models.IntegerField()),
                ('base_ad', models.FloatField()),
                ('base_as', models.IntegerField()),
                ('base_ar', models.FloatField()),
                ('base_mr', models.FloatField()),
                ('base_hp5', models.FloatField()),
                ('base_mp5', models.FloatField()),
                ('base_movement_speed', models.IntegerField()),
                ('base_range', models.IntegerField()),
                ('ad_per_lvl', models.FloatField()),
                ('as_per_lvl', models.FloatField()),
                ('ar_per_lvl', models.FloatField()),
                ('mr_per_lvl', models.FloatField()),
                ('hp_per_lvl', models.FloatField()),
                ('mp_per_lvl', models.FloatField()),
                ('hp5_per_lvl', models.FloatField()),
                ('mp5_per_lvl', models.FloatField()),
                ('skill_passive', models.TextField()),
                ('skill_q', models.TextField()),
                ('skill_q_cd1', models.FloatField()),
                ('skill_q_cd2', models.FloatField()),
                ('skill_q_cd3', models.FloatField()),
                ('skill_q_cd4', models.FloatField()),
                ('skill_q_cd5', models.FloatField()),
                ('skill_q_cost1', models.IntegerField()),
                ('skill_q_cost2', models.IntegerField()),
                ('skill_q_cost3', models.IntegerField()),
                ('skill_q_cost4', models.IntegerField()),
                ('skill_q_cost5', models.IntegerField()),
                ('skill_w', models.TextField()),
                ('skill_w_cd1', models.FloatField()),
                ('skill_w_cd2', models.FloatField()),
                ('skill_w_cd3', models.FloatField()),
                ('skill_w_cd4', models.FloatField()),
                ('skill_w_cd5', models.FloatField()),
                ('skill_w_cost1', models.IntegerField()),
                ('skill_w_cost2', models.IntegerField()),
                ('skill_w_cost3', models.IntegerField()),
                ('skill_w_cost4', models.IntegerField()),
                ('skill_w_cost5', models.IntegerField()),
                ('skill_e', models.TextField()),
                ('skill_e_cd1', models.FloatField()),
                ('skill_e_cd2', models.FloatField()),
                ('skill_e_cd3', models.FloatField()),
                ('skill_e_cd4', models.FloatField()),
                ('skill_e_cd5', models.FloatField()),
                ('skill_e_cost1', models.IntegerField()),
                ('skill_e_cost2', models.IntegerField()),
                ('skill_e_cost3', models.IntegerField()),
                ('skill_e_cost4', models.IntegerField()),
                ('skill_e_cost5', models.IntegerField()),
                ('skill_r', models.TextField()),
                ('skill_r_cd1', models.FloatField()),
                ('skill_r_cd2', models.FloatField()),
                ('skill_r_cd3', models.FloatField()),
                ('skill_r_cost1', models.IntegerField()),
                ('skill_r_cost2', models.IntegerField()),
                ('skill_r_cost3', models.IntegerField()),
            ],
        ),
    ]
