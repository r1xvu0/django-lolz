from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import CustomChampion, CustomItem

class NameForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    surname = forms.CharField(label="Surname", max_length=100)

class CreateChampionForm(forms.Form):
    champion_name = forms.CharField(label="Champion Name", max_length=100)
    champion_title = forms.CharField(label="Title", max_length=50)
    champion_lore = forms.CharField(label="Lore")
    champion_role = forms.ChoiceField(choices = (("controller", "Controller"), ("fighter", "Fighter"),("mage", "Mage"), ("marksman" ,"Marksman"),("slayer", "Slayer"), ("tank", "Tank"), ("specialist", "Specialist"))
    )

# MODEL TO FORM
# class TestModelForm(forms.ModelForm):
#     class Meta:
#         model = TestModel
#         fields = ["firstname", "lastname", "email", "comment"]

class ChampionForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    class Meta:
        model = CustomChampion
        fields = [
            "name",
            "title",
            "role",
            "lore",
            "resource",
            "base_hp",
            "base_mp",
            "base_ad",
            "base_as",
            "base_ar",
            "base_mr",
            "base_hp5",
            "base_mp5",
            "base_movement_speed",
            "base_range",
            "ad_per_lvl",
            "as_per_lvl",
            "ar_per_lvl",
            "mr_per_lvl",
            "hp_per_lvl",
            "mp_per_lvl",
            "hp5_per_lvl",
            "mp5_per_lvl",
            "skill_passive_name",
            "skill_passive",
            "skill_passive_icon",
            "skill_q_name",
            "skill_q",
            "skill_q_icon",
            "skill_q_cd1",
            "skill_q_cd2",
            "skill_q_cd3",
            "skill_q_cd4",
            "skill_q_cd5",
            "skill_q_cost1",
            "skill_q_cost2",
            "skill_q_cost3",
            "skill_q_cost4",
            "skill_q_cost5",
            "skill_w_name",
            "skill_w",
            "skill_w_icon",
            "skill_w_cd1",
            "skill_w_cd2",
            "skill_w_cd3",
            "skill_w_cd4",
            "skill_w_cd5",
            "skill_w_cost1",
            "skill_w_cost2",
            "skill_w_cost3",
            "skill_w_cost4",
            "skill_w_cost5",
            "skill_e_name",
            "skill_e",
            "skill_e_icon",
            "skill_e_cd1",
            "skill_e_cd2",
            "skill_e_cd3",
            "skill_e_cd4",
            "skill_e_cd5",
            "skill_e_cost1",
            "skill_e_cost2",
            "skill_e_cost3",
            "skill_e_cost4",
            "skill_e_cost5",
            "skill_r_name",
            "skill_r",
            "skill_r_icon",
            "skill_r_cd1",
            "skill_r_cd2",
            "skill_r_cd3",
            "skill_r_cost1",
            "skill_r_cost2",
            "skill_r_cost3",
        ]

class ItemForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    class Meta:
        model = CustomItem
        fields = [
            "name",
            "image_url",
            "lore",
            "type",
            "cost",
            "combine_cost",
            "sell_cost",
            "stat1",
            "stat1_value",
            "stat2",
            "stat2_value",
            "stat3",
            "stat3_value",
            "stat4",
            "stat4_value",
            "passive_stat_name",
            "passive_stat",
            "passive_stat_unique",
            "active_stat_name",
            "active_stat",
            "active_stat_unique",
        ]

        def __str__(self):
            ret = self.name
            return ret