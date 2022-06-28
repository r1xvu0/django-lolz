import uuid
from django.db import models
from autoslug import AutoSlugField
from django.forms import SlugField

# Create your models here.
'''
MODELS HERE
'''
# class TestModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     email = models.EmailField()
#     comment = models.CharField(max_length=10000)

#     def __str__(self):
#         ret = self.firstname + " " + self.lastname + " - " + self.comment + " | " + str(self.id)
#         return ret

class CustomChampion(models.Model):
    ROLES = (
        ('controller', 'Controller'),
        ('fighter', 'Fighter'),
        ('mage', 'Mage'),
        ('marksman', 'Marksman'),
        ('slayer', 'Slayer'),
        ('tank', 'Tank'),
        ('specialist', 'Specialist'),
    )
    RESOURCES = (
        ('mana', 'Mana'),
        ('health', 'Health'),
        ('energy', 'Energy'),
        ('rage', 'Rage'),
        ('focus', 'Focus'),
        ('runic_power', 'Runic Power'),
        ('none', 'None'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='title', unique_with='name')
    name = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    role = models.CharField(choices=ROLES, max_length=20, default=0,  blank=False)
    lore = models.TextField(blank=True)
    resource = models.CharField(choices=RESOURCES, max_length=20, default=0,  blank=False)
    base_hp = models.IntegerField(blank=False)
    base_mp = models.IntegerField(blank=False)
    base_ad = models.FloatField(blank=False)
    base_as = models.FloatField(blank=False)
    base_ar = models.FloatField(blank=False)
    base_mr = models.FloatField(blank=False)
    base_hp5 = models.FloatField(blank=False)
    base_mp5 = models.FloatField(blank=False)
    base_movement_speed = models.IntegerField(blank=False)
    base_range = models.IntegerField(blank=False)
    ad_per_lvl = models.FloatField(blank=False)
    as_per_lvl = models.FloatField(blank=False)
    ar_per_lvl = models.FloatField(blank=False)
    mr_per_lvl = models.FloatField(blank=False)
    hp_per_lvl = models.FloatField(blank=False)
    mp_per_lvl = models.FloatField(blank=False)
    hp5_per_lvl = models.FloatField(blank=False)
    mp5_per_lvl = models.FloatField(blank=False)
    skill_passive_name = models.CharField(max_length=100, blank=False)
    skill_passive = models.TextField(blank=False)
    skill_passive_icon = models.CharField(max_length=1000, blank=False)
    skill_q_name = models.CharField(max_length=100, blank=False)
    skill_q = models.TextField(blank=False)
    skill_q_icon = models.CharField(max_length=1000, blank=False)
    skill_q_cd1 = models.FloatField(blank=False)
    skill_q_cd2 = models.FloatField(blank=False)
    skill_q_cd3 = models.FloatField(blank=False)
    skill_q_cd4 = models.FloatField(blank=False)
    skill_q_cd5 = models.FloatField(blank=False)
    skill_q_cost1 = models.IntegerField(blank=False)
    skill_q_cost2 = models.IntegerField(blank=False)
    skill_q_cost3 = models.IntegerField(blank=False)
    skill_q_cost4 = models.IntegerField(blank=False)
    skill_q_cost5 = models.IntegerField(blank=False)
    skill_w_name = models.CharField(max_length=100, blank=False)
    skill_w = models.TextField(blank=False)
    skill_w_icon = models.CharField(max_length=1000, blank=False)
    skill_w_cd1 = models.FloatField(blank=False)
    skill_w_cd2 = models.FloatField(blank=False)
    skill_w_cd3 = models.FloatField(blank=False)
    skill_w_cd4 = models.FloatField(blank=False)
    skill_w_cd5 = models.FloatField(blank=False)
    skill_w_cost1 = models.IntegerField(blank=False)
    skill_w_cost2 = models.IntegerField(blank=False)
    skill_w_cost3 = models.IntegerField(blank=False)
    skill_w_cost4 = models.IntegerField(blank=False)
    skill_w_cost5 = models.IntegerField(blank=False)
    skill_e_name = models.CharField(max_length=100, blank=False)
    skill_e = models.TextField(blank=False)
    skill_e_icon = models.CharField(max_length=1000, blank=False)
    skill_e_cd1 = models.FloatField(blank=False)
    skill_e_cd2 = models.FloatField(blank=False)
    skill_e_cd3 = models.FloatField(blank=False)
    skill_e_cd4 = models.FloatField(blank=False)
    skill_e_cd5 = models.FloatField(blank=False)
    skill_e_cost1 = models.IntegerField(blank=False)
    skill_e_cost2 = models.IntegerField(blank=False)
    skill_e_cost3 = models.IntegerField(blank=False)
    skill_e_cost4 = models.IntegerField(blank=False)
    skill_e_cost5 = models.IntegerField(blank=False)
    skill_r_name = models.CharField(max_length=100, blank=False)
    skill_r = models.TextField(blank=False)
    skill_r_icon = models.CharField(max_length=1000, blank=False)
    skill_r_cd1 = models.FloatField(blank=False)
    skill_r_cd2 = models.FloatField(blank=False)
    skill_r_cd3 = models.FloatField(blank=False)
    skill_r_cost1 = models.IntegerField(blank=False)
    skill_r_cost2 = models.IntegerField(blank=False)
    skill_r_cost3 = models.IntegerField(blank=False)

    def __str__(self):
        ret = self.name + " - " + self.title + " - " + self.slug
        return ret
    

class CustomItem(models.Model):
    STATS = (
        ('Attack Damage', 'Attack Damage'),
        ('Ability Power', 'Ability Power'),
        ('Attack Speed', 'Attack Speed'),
        ('Ability Haste', 'Ability Haste'),
        ('Critical Chance', 'Critical Chance'),
        ('Critical Damage', 'Critical Damage'),
        ('Life Steal', "Life Steal"),
        ('Armor Penetration', "Armor Penetration"),
        ('Magic Penetration', "Magic Penetration"),
        ('Lethality', "Lethality"),
        ('Mana', "Mana"),
        ('Mana Regen / 5s', "Mana Regen / 5s"),
        ('Mana Regen', "Mana Regen"),
        ('Health', "Health"),
        ('Health Regen / 5s', "Health Regen / 5s"),
        ('Health Regen %', "Health Regen %"),
        ('Heal and Shield Power', "Heal and Shield Power"),
        ('Omni-Vamp', "Omni-Vamp"),
        ('Armor', "Armor"),
        ('Magic Resist', "Magic Resist"),
        ('Movement Speed', "Movement Speed"),
    )
    TYPES = (
        ('Starter', 'Starter'),
        ('Basic', 'Basic'),
        ('Epic', 'Epic'),
        ('Legendary', 'Legendary'),
        ('Mythic', 'Mythic'),
        ('Consumable', 'Consumable'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from='name', unique_with='name')
    name = models.CharField(max_length=100, blank=False)
    image_url = models.CharField(max_length=1000, blank=True)
    lore = models.TextField(blank=True)
    type = models.CharField(choices=TYPES, max_length=100, blank=False)
    stat1 = models.CharField(choices=STATS, max_length=25, default=0, null=True, blank=False)
    stat1_value = models.FloatField(blank=False)
    stat2 = models.CharField(choices=STATS, max_length=25, default=0, null=True, blank=True)
    stat2_value = models.FloatField(null=True, blank=True)
    stat3 = models.CharField(choices=STATS, max_length=25, default=0, null=True, blank=True)
    stat3_value = models.FloatField(null=True, blank=True)
    stat4 = models.CharField(choices=STATS, max_length=25, default=0, null=True, blank=True)
    stat4_value = models.FloatField(null=True, blank=True)
    passive_stat_name = models.CharField(max_length=100, blank=True)
    passive_stat = models.TextField(blank=True)
    passive_stat_unique = models.BooleanField(default=True, help_text="Is Unique?")
    active_stat_name = models.CharField(max_length=100, blank=True)
    active_stat = models.TextField(blank=True)
    active_stat_unique = models.BooleanField(default=True, help_text="Is Unique?")
    cost = models.IntegerField(blank=False)
    combine_cost = models.IntegerField(blank=False)
    sell_cost = models.IntegerField(blank=False)

    def __str__(self):
        ret = self.name
        return ret