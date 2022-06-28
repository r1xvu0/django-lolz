# Generated by Django 4.0.5 on 2022-06-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_customitem_stat1_customitem_stat1_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customitem',
            name='active_stat',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customitem',
            name='passive_stat',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='stat1',
            field=models.CharField(choices=[('ad', 'Attack Damage'), ('ap', 'Ability Power'), ('as', 'Attack Speed'), ('ah', 'Ability Haste'), ('crit', 'Critical Chance'), ('critdmg', 'Critical Damage'), ('ls', 'Life Steal'), ('apen', 'Armor Penetration'), ('mapen', 'Magic Armor Penetration'), ('lethality', 'Lethality'), ('mp', 'Mana'), ('mp5', 'Mana Regen'), ('hp', 'Health'), ('hp5', 'Health Regen'), ('hsp', 'Heal and Shield Power'), ('ovamp', 'Omni-Vamp'), ('armor', 'Armor'), ('mr', 'Magic Resist'), ('ms', 'Movement Speed')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='stat2',
            field=models.CharField(blank=True, choices=[('ad', 'Attack Damage'), ('ap', 'Ability Power'), ('as', 'Attack Speed'), ('ah', 'Ability Haste'), ('crit', 'Critical Chance'), ('critdmg', 'Critical Damage'), ('ls', 'Life Steal'), ('apen', 'Armor Penetration'), ('mapen', 'Magic Armor Penetration'), ('lethality', 'Lethality'), ('mp', 'Mana'), ('mp5', 'Mana Regen'), ('hp', 'Health'), ('hp5', 'Health Regen'), ('hsp', 'Heal and Shield Power'), ('ovamp', 'Omni-Vamp'), ('armor', 'Armor'), ('mr', 'Magic Resist'), ('ms', 'Movement Speed')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='stat3',
            field=models.CharField(blank=True, choices=[('ad', 'Attack Damage'), ('ap', 'Ability Power'), ('as', 'Attack Speed'), ('ah', 'Ability Haste'), ('crit', 'Critical Chance'), ('critdmg', 'Critical Damage'), ('ls', 'Life Steal'), ('apen', 'Armor Penetration'), ('mapen', 'Magic Armor Penetration'), ('lethality', 'Lethality'), ('mp', 'Mana'), ('mp5', 'Mana Regen'), ('hp', 'Health'), ('hp5', 'Health Regen'), ('hsp', 'Heal and Shield Power'), ('ovamp', 'Omni-Vamp'), ('armor', 'Armor'), ('mr', 'Magic Resist'), ('ms', 'Movement Speed')], default=0, max_length=20),
        ),
    ]
