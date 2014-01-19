# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Character.base_attack_bonus'
        db.delete_column(u'main_character', 'base_attack_bonus')

        # Adding field 'Character.alignment'
        db.add_column(u'main_character', 'alignment',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=20),
                      keep_default=False)

        # Adding field 'Character.race'
        db.add_column(u'main_character', 'race',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=20),
                      keep_default=False)

        # Adding field 'Character.deity'
        db.add_column(u'main_character', 'deity',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=20),
                      keep_default=False)

        # Adding field 'Character.size'
        db.add_column(u'main_character', 'size',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=20),
                      keep_default=False)

        # Adding field 'Character.gender'
        db.add_column(u'main_character', 'gender',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=20),
                      keep_default=False)

        # Adding field 'Character.age'
        db.add_column(u'main_character', 'age',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.height'
        db.add_column(u'main_character', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.weight'
        db.add_column(u'main_character', 'weight',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.hair'
        db.add_column(u'main_character', 'hair',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=20),
                      keep_default=False)

        # Adding field 'Character.eyes'
        db.add_column(u'main_character', 'eyes',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=20),
                      keep_default=False)

        # Adding field 'Character.ability_str_mod'
        db.add_column(u'main_character', 'ability_str_mod',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_str_temp'
        db.add_column(u'main_character', 'ability_str_temp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_dex_mod'
        db.add_column(u'main_character', 'ability_dex_mod',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_dex_temp'
        db.add_column(u'main_character', 'ability_dex_temp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_con_mod'
        db.add_column(u'main_character', 'ability_con_mod',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_con_temp'
        db.add_column(u'main_character', 'ability_con_temp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_wis_mod'
        db.add_column(u'main_character', 'ability_wis_mod',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_wis_temp'
        db.add_column(u'main_character', 'ability_wis_temp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_int_mod'
        db.add_column(u'main_character', 'ability_int_mod',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_int_temp'
        db.add_column(u'main_character', 'ability_int_temp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_cha_mod'
        db.add_column(u'main_character', 'ability_cha_mod',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ability_cha_temp'
        db.add_column(u'main_character', 'ability_cha_temp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.speed_normal'
        db.add_column(u'main_character', 'speed_normal',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.speed_armor'
        db.add_column(u'main_character', 'speed_armor',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.speed_fly'
        db.add_column(u'main_character', 'speed_fly',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.speed_swim'
        db.add_column(u'main_character', 'speed_swim',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.speed_climb'
        db.add_column(u'main_character', 'speed_climb',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.initiative'
        db.add_column(u'main_character', 'initiative',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.initiative_misc'
        db.add_column(u'main_character', 'initiative_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.bab'
        db.add_column(u'main_character', 'bab',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.spell_resistance'
        db.add_column(u'main_character', 'spell_resistance',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ac_natural'
        db.add_column(u'main_character', 'ac_natural',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ac_misc'
        db.add_column(u'main_character', 'ac_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ac_armor'
        db.add_column(u'main_character', 'ac_armor',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.ac_shield'
        db.add_column(u'main_character', 'ac_shield',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.cmb'
        db.add_column(u'main_character', 'cmb',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_acrobatics'
        db.add_column(u'main_character', 'sk_acrobatics',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_acrobatics_ranks'
        db.add_column(u'main_character', 'sk_acrobatics_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_acrobatics_misc'
        db.add_column(u'main_character', 'sk_acrobatics_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_acrobatics_class'
        db.add_column(u'main_character', 'sk_acrobatics_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_appraise'
        db.add_column(u'main_character', 'sk_appraise',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_appraise_ranks'
        db.add_column(u'main_character', 'sk_appraise_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_appraise_misc'
        db.add_column(u'main_character', 'sk_appraise_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_appraise_class'
        db.add_column(u'main_character', 'sk_appraise_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_bluff'
        db.add_column(u'main_character', 'sk_bluff',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_bluff_ranks'
        db.add_column(u'main_character', 'sk_bluff_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_bluff_misc'
        db.add_column(u'main_character', 'sk_bluff_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_bluff_class'
        db.add_column(u'main_character', 'sk_bluff_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_climb'
        db.add_column(u'main_character', 'sk_climb',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_climb_ranks'
        db.add_column(u'main_character', 'sk_climb_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_climb_misc'
        db.add_column(u'main_character', 'sk_climb_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_climb_class'
        db.add_column(u'main_character', 'sk_climb_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_craft_type'
        db.add_column(u'main_character', 'sk_craft_type',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=20),
                      keep_default=False)

        # Adding field 'Character.sk_craft'
        db.add_column(u'main_character', 'sk_craft',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_craft_ranks'
        db.add_column(u'main_character', 'sk_craft_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_craft_misc'
        db.add_column(u'main_character', 'sk_craft_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_craft_class'
        db.add_column(u'main_character', 'sk_craft_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_diplomacy'
        db.add_column(u'main_character', 'sk_diplomacy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_diplomacy_ranks'
        db.add_column(u'main_character', 'sk_diplomacy_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_diplomacy_misc'
        db.add_column(u'main_character', 'sk_diplomacy_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_diplomacy_class'
        db.add_column(u'main_character', 'sk_diplomacy_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_disable_devie'
        db.add_column(u'main_character', 'sk_disable_devie',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_disable_device_ranks'
        db.add_column(u'main_character', 'sk_disable_device_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_disable_device_misc'
        db.add_column(u'main_character', 'sk_disable_device_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_disable_device_class'
        db.add_column(u'main_character', 'sk_disable_device_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_disguise'
        db.add_column(u'main_character', 'sk_disguise',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_disguise_ranks'
        db.add_column(u'main_character', 'sk_disguise_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_disguise_misc'
        db.add_column(u'main_character', 'sk_disguise_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_disguise_class'
        db.add_column(u'main_character', 'sk_disguise_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_escape_artist'
        db.add_column(u'main_character', 'sk_escape_artist',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_escape_artist_ranks'
        db.add_column(u'main_character', 'sk_escape_artist_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_escape_artist_misc'
        db.add_column(u'main_character', 'sk_escape_artist_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_escape_artist_class'
        db.add_column(u'main_character', 'sk_escape_artist_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_fly'
        db.add_column(u'main_character', 'sk_fly',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_fly_ranks'
        db.add_column(u'main_character', 'sk_fly_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_fly_misc'
        db.add_column(u'main_character', 'sk_fly_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_fly_class'
        db.add_column(u'main_character', 'sk_fly_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_handle_animal'
        db.add_column(u'main_character', 'sk_handle_animal',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_handle_animal_ranks'
        db.add_column(u'main_character', 'sk_handle_animal_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_handle_animal_misc'
        db.add_column(u'main_character', 'sk_handle_animal_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_handle_animal_class'
        db.add_column(u'main_character', 'sk_handle_animal_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_heal'
        db.add_column(u'main_character', 'sk_heal',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_heal_ranks'
        db.add_column(u'main_character', 'sk_heal_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_heal_misc'
        db.add_column(u'main_character', 'sk_heal_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_heal_class'
        db.add_column(u'main_character', 'sk_heal_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_intimidate'
        db.add_column(u'main_character', 'sk_intimidate',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_intimidate_ranks'
        db.add_column(u'main_character', 'sk_intimidate_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_intimidate_misc'
        db.add_column(u'main_character', 'sk_intimidate_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_intimidate_class'
        db.add_column(u'main_character', 'sk_intimidate_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_arcana'
        db.add_column(u'main_character', 'sk_knowledge_arcana',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_arcana_ranks'
        db.add_column(u'main_character', 'sk_knowledge_arcana_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_arcana_misc'
        db.add_column(u'main_character', 'sk_knowledge_arcana_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_arcana_class'
        db.add_column(u'main_character', 'sk_knowledge_arcana_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_dungeoneering'
        db.add_column(u'main_character', 'sk_knowledge_dungeoneering',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_dungeoneering_ranks'
        db.add_column(u'main_character', 'sk_knowledge_dungeoneering_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_dungeoneering_misc'
        db.add_column(u'main_character', 'sk_knowledge_dungeoneering_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_dungeoneering_class'
        db.add_column(u'main_character', 'sk_knowledge_dungeoneering_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_engineering'
        db.add_column(u'main_character', 'sk_knowledge_engineering',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_engineering_ranks'
        db.add_column(u'main_character', 'sk_knowledge_engineering_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_engineering_misc'
        db.add_column(u'main_character', 'sk_knowledge_engineering_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_engineering_class'
        db.add_column(u'main_character', 'sk_knowledge_engineering_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_geography'
        db.add_column(u'main_character', 'sk_knowledge_geography',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_geography_ranks'
        db.add_column(u'main_character', 'sk_knowledge_geography_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_geography_misc'
        db.add_column(u'main_character', 'sk_knowledge_geography_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_geography_class'
        db.add_column(u'main_character', 'sk_knowledge_geography_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_history'
        db.add_column(u'main_character', 'sk_knowledge_history',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_history_ranks'
        db.add_column(u'main_character', 'sk_knowledge_history_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_history_misc'
        db.add_column(u'main_character', 'sk_knowledge_history_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_history_class'
        db.add_column(u'main_character', 'sk_knowledge_history_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_local'
        db.add_column(u'main_character', 'sk_knowledge_local',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_local_ranks'
        db.add_column(u'main_character', 'sk_knowledge_local_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_local_misc'
        db.add_column(u'main_character', 'sk_knowledge_local_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_local_class'
        db.add_column(u'main_character', 'sk_knowledge_local_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_nature'
        db.add_column(u'main_character', 'sk_knowledge_nature',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_nature_ranks'
        db.add_column(u'main_character', 'sk_knowledge_nature_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_nature_misc'
        db.add_column(u'main_character', 'sk_knowledge_nature_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_nature_class'
        db.add_column(u'main_character', 'sk_knowledge_nature_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_nobility'
        db.add_column(u'main_character', 'sk_knowledge_nobility',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_nobility_ranks'
        db.add_column(u'main_character', 'sk_knowledge_nobility_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_nobility_misc'
        db.add_column(u'main_character', 'sk_knowledge_nobility_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_nobility_class'
        db.add_column(u'main_character', 'sk_knowledge_nobility_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_planes'
        db.add_column(u'main_character', 'sk_knowledge_planes',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_planes_ranks'
        db.add_column(u'main_character', 'sk_knowledge_planes_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_planes_misc'
        db.add_column(u'main_character', 'sk_knowledge_planes_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_planes_class'
        db.add_column(u'main_character', 'sk_knowledge_planes_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_religion'
        db.add_column(u'main_character', 'sk_knowledge_religion',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_religion_ranks'
        db.add_column(u'main_character', 'sk_knowledge_religion_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_religion_misc'
        db.add_column(u'main_character', 'sk_knowledge_religion_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_knowledge_religion_class'
        db.add_column(u'main_character', 'sk_knowledge_religion_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_linguistics'
        db.add_column(u'main_character', 'sk_linguistics',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_linguistics_ranks'
        db.add_column(u'main_character', 'sk_linguistics_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_linguistics_misc'
        db.add_column(u'main_character', 'sk_linguistics_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_linguistics_class'
        db.add_column(u'main_character', 'sk_linguistics_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_perception'
        db.add_column(u'main_character', 'sk_perception',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_perception_ranks'
        db.add_column(u'main_character', 'sk_perception_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_perception_misc'
        db.add_column(u'main_character', 'sk_perception_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_perform'
        db.add_column(u'main_character', 'sk_perform',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_perform_ranks'
        db.add_column(u'main_character', 'sk_perform_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_perform_misc'
        db.add_column(u'main_character', 'sk_perform_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_perception_class'
        db.add_column(u'main_character', 'sk_perception_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_profession_type'
        db.add_column(u'main_character', 'sk_profession_type',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=20),
                      keep_default=False)

        # Adding field 'Character.sk_profession'
        db.add_column(u'main_character', 'sk_profession',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_profession_ranks'
        db.add_column(u'main_character', 'sk_profession_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_profession_misc'
        db.add_column(u'main_character', 'sk_profession_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_profession_class'
        db.add_column(u'main_character', 'sk_profession_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_ride'
        db.add_column(u'main_character', 'sk_ride',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_ride_ranks'
        db.add_column(u'main_character', 'sk_ride_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_ride_misc'
        db.add_column(u'main_character', 'sk_ride_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_ride_class'
        db.add_column(u'main_character', 'sk_ride_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_sense_motive'
        db.add_column(u'main_character', 'sk_sense_motive',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_sense_motive_ranks'
        db.add_column(u'main_character', 'sk_sense_motive_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_sense_motive_misc'
        db.add_column(u'main_character', 'sk_sense_motive_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_sense_motive_class'
        db.add_column(u'main_character', 'sk_sense_motive_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_sleight_of_hand'
        db.add_column(u'main_character', 'sk_sleight_of_hand',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_sleight_of_hand_ranks'
        db.add_column(u'main_character', 'sk_sleight_of_hand_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_sleight_of_hand_misc'
        db.add_column(u'main_character', 'sk_sleight_of_hand_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_sleight_of_hand_class'
        db.add_column(u'main_character', 'sk_sleight_of_hand_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_spellcraft'
        db.add_column(u'main_character', 'sk_spellcraft',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_spellcraft_ranks'
        db.add_column(u'main_character', 'sk_spellcraft_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_spellcraft_misc'
        db.add_column(u'main_character', 'sk_spellcraft_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_spellcraft_class'
        db.add_column(u'main_character', 'sk_spellcraft_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_stealth'
        db.add_column(u'main_character', 'sk_stealth',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_stealth_ranks'
        db.add_column(u'main_character', 'sk_stealth_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_steahth_misc'
        db.add_column(u'main_character', 'sk_steahth_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_stealth_class'
        db.add_column(u'main_character', 'sk_stealth_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_survival'
        db.add_column(u'main_character', 'sk_survival',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_survival_ranks'
        db.add_column(u'main_character', 'sk_survival_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_survival_misc'
        db.add_column(u'main_character', 'sk_survival_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_survival_class'
        db.add_column(u'main_character', 'sk_survival_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_swim'
        db.add_column(u'main_character', 'sk_swim',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_swim_ranks'
        db.add_column(u'main_character', 'sk_swim_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_swim_misc'
        db.add_column(u'main_character', 'sk_swim_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_swim_class'
        db.add_column(u'main_character', 'sk_swim_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Character.sk_use_magical_device'
        db.add_column(u'main_character', 'sk_use_magical_device',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_use_magical_device_ranks'
        db.add_column(u'main_character', 'sk_use_magical_device_ranks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_use_magical_device_misc'
        db.add_column(u'main_character', 'sk_use_magical_device_misc',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Character.sk_use_magical_device_class'
        db.add_column(u'main_character', 'sk_use_magical_device_class',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Character.base_attack_bonus'
        db.add_column(u'main_character', 'base_attack_bonus',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Character.alignment'
        db.delete_column(u'main_character', 'alignment')

        # Deleting field 'Character.race'
        db.delete_column(u'main_character', 'race')

        # Deleting field 'Character.deity'
        db.delete_column(u'main_character', 'deity')

        # Deleting field 'Character.size'
        db.delete_column(u'main_character', 'size')

        # Deleting field 'Character.gender'
        db.delete_column(u'main_character', 'gender')

        # Deleting field 'Character.age'
        db.delete_column(u'main_character', 'age')

        # Deleting field 'Character.height'
        db.delete_column(u'main_character', 'height')

        # Deleting field 'Character.weight'
        db.delete_column(u'main_character', 'weight')

        # Deleting field 'Character.hair'
        db.delete_column(u'main_character', 'hair')

        # Deleting field 'Character.eyes'
        db.delete_column(u'main_character', 'eyes')

        # Deleting field 'Character.ability_str_mod'
        db.delete_column(u'main_character', 'ability_str_mod')

        # Deleting field 'Character.ability_str_temp'
        db.delete_column(u'main_character', 'ability_str_temp')

        # Deleting field 'Character.ability_dex_mod'
        db.delete_column(u'main_character', 'ability_dex_mod')

        # Deleting field 'Character.ability_dex_temp'
        db.delete_column(u'main_character', 'ability_dex_temp')

        # Deleting field 'Character.ability_con_mod'
        db.delete_column(u'main_character', 'ability_con_mod')

        # Deleting field 'Character.ability_con_temp'
        db.delete_column(u'main_character', 'ability_con_temp')

        # Deleting field 'Character.ability_wis_mod'
        db.delete_column(u'main_character', 'ability_wis_mod')

        # Deleting field 'Character.ability_wis_temp'
        db.delete_column(u'main_character', 'ability_wis_temp')

        # Deleting field 'Character.ability_int_mod'
        db.delete_column(u'main_character', 'ability_int_mod')

        # Deleting field 'Character.ability_int_temp'
        db.delete_column(u'main_character', 'ability_int_temp')

        # Deleting field 'Character.ability_cha_mod'
        db.delete_column(u'main_character', 'ability_cha_mod')

        # Deleting field 'Character.ability_cha_temp'
        db.delete_column(u'main_character', 'ability_cha_temp')

        # Deleting field 'Character.speed_normal'
        db.delete_column(u'main_character', 'speed_normal')

        # Deleting field 'Character.speed_armor'
        db.delete_column(u'main_character', 'speed_armor')

        # Deleting field 'Character.speed_fly'
        db.delete_column(u'main_character', 'speed_fly')

        # Deleting field 'Character.speed_swim'
        db.delete_column(u'main_character', 'speed_swim')

        # Deleting field 'Character.speed_climb'
        db.delete_column(u'main_character', 'speed_climb')

        # Deleting field 'Character.initiative'
        db.delete_column(u'main_character', 'initiative')

        # Deleting field 'Character.initiative_misc'
        db.delete_column(u'main_character', 'initiative_misc')

        # Deleting field 'Character.bab'
        db.delete_column(u'main_character', 'bab')

        # Deleting field 'Character.spell_resistance'
        db.delete_column(u'main_character', 'spell_resistance')

        # Deleting field 'Character.ac_natural'
        db.delete_column(u'main_character', 'ac_natural')

        # Deleting field 'Character.ac_misc'
        db.delete_column(u'main_character', 'ac_misc')

        # Deleting field 'Character.ac_armor'
        db.delete_column(u'main_character', 'ac_armor')

        # Deleting field 'Character.ac_shield'
        db.delete_column(u'main_character', 'ac_shield')

        # Deleting field 'Character.cmb'
        db.delete_column(u'main_character', 'cmb')

        # Deleting field 'Character.sk_acrobatics'
        db.delete_column(u'main_character', 'sk_acrobatics')

        # Deleting field 'Character.sk_acrobatics_ranks'
        db.delete_column(u'main_character', 'sk_acrobatics_ranks')

        # Deleting field 'Character.sk_acrobatics_misc'
        db.delete_column(u'main_character', 'sk_acrobatics_misc')

        # Deleting field 'Character.sk_acrobatics_class'
        db.delete_column(u'main_character', 'sk_acrobatics_class')

        # Deleting field 'Character.sk_appraise'
        db.delete_column(u'main_character', 'sk_appraise')

        # Deleting field 'Character.sk_appraise_ranks'
        db.delete_column(u'main_character', 'sk_appraise_ranks')

        # Deleting field 'Character.sk_appraise_misc'
        db.delete_column(u'main_character', 'sk_appraise_misc')

        # Deleting field 'Character.sk_appraise_class'
        db.delete_column(u'main_character', 'sk_appraise_class')

        # Deleting field 'Character.sk_bluff'
        db.delete_column(u'main_character', 'sk_bluff')

        # Deleting field 'Character.sk_bluff_ranks'
        db.delete_column(u'main_character', 'sk_bluff_ranks')

        # Deleting field 'Character.sk_bluff_misc'
        db.delete_column(u'main_character', 'sk_bluff_misc')

        # Deleting field 'Character.sk_bluff_class'
        db.delete_column(u'main_character', 'sk_bluff_class')

        # Deleting field 'Character.sk_climb'
        db.delete_column(u'main_character', 'sk_climb')

        # Deleting field 'Character.sk_climb_ranks'
        db.delete_column(u'main_character', 'sk_climb_ranks')

        # Deleting field 'Character.sk_climb_misc'
        db.delete_column(u'main_character', 'sk_climb_misc')

        # Deleting field 'Character.sk_climb_class'
        db.delete_column(u'main_character', 'sk_climb_class')

        # Deleting field 'Character.sk_craft_type'
        db.delete_column(u'main_character', 'sk_craft_type')

        # Deleting field 'Character.sk_craft'
        db.delete_column(u'main_character', 'sk_craft')

        # Deleting field 'Character.sk_craft_ranks'
        db.delete_column(u'main_character', 'sk_craft_ranks')

        # Deleting field 'Character.sk_craft_misc'
        db.delete_column(u'main_character', 'sk_craft_misc')

        # Deleting field 'Character.sk_craft_class'
        db.delete_column(u'main_character', 'sk_craft_class')

        # Deleting field 'Character.sk_diplomacy'
        db.delete_column(u'main_character', 'sk_diplomacy')

        # Deleting field 'Character.sk_diplomacy_ranks'
        db.delete_column(u'main_character', 'sk_diplomacy_ranks')

        # Deleting field 'Character.sk_diplomacy_misc'
        db.delete_column(u'main_character', 'sk_diplomacy_misc')

        # Deleting field 'Character.sk_diplomacy_class'
        db.delete_column(u'main_character', 'sk_diplomacy_class')

        # Deleting field 'Character.sk_disable_devie'
        db.delete_column(u'main_character', 'sk_disable_devie')

        # Deleting field 'Character.sk_disable_device_ranks'
        db.delete_column(u'main_character', 'sk_disable_device_ranks')

        # Deleting field 'Character.sk_disable_device_misc'
        db.delete_column(u'main_character', 'sk_disable_device_misc')

        # Deleting field 'Character.sk_disable_device_class'
        db.delete_column(u'main_character', 'sk_disable_device_class')

        # Deleting field 'Character.sk_disguise'
        db.delete_column(u'main_character', 'sk_disguise')

        # Deleting field 'Character.sk_disguise_ranks'
        db.delete_column(u'main_character', 'sk_disguise_ranks')

        # Deleting field 'Character.sk_disguise_misc'
        db.delete_column(u'main_character', 'sk_disguise_misc')

        # Deleting field 'Character.sk_disguise_class'
        db.delete_column(u'main_character', 'sk_disguise_class')

        # Deleting field 'Character.sk_escape_artist'
        db.delete_column(u'main_character', 'sk_escape_artist')

        # Deleting field 'Character.sk_escape_artist_ranks'
        db.delete_column(u'main_character', 'sk_escape_artist_ranks')

        # Deleting field 'Character.sk_escape_artist_misc'
        db.delete_column(u'main_character', 'sk_escape_artist_misc')

        # Deleting field 'Character.sk_escape_artist_class'
        db.delete_column(u'main_character', 'sk_escape_artist_class')

        # Deleting field 'Character.sk_fly'
        db.delete_column(u'main_character', 'sk_fly')

        # Deleting field 'Character.sk_fly_ranks'
        db.delete_column(u'main_character', 'sk_fly_ranks')

        # Deleting field 'Character.sk_fly_misc'
        db.delete_column(u'main_character', 'sk_fly_misc')

        # Deleting field 'Character.sk_fly_class'
        db.delete_column(u'main_character', 'sk_fly_class')

        # Deleting field 'Character.sk_handle_animal'
        db.delete_column(u'main_character', 'sk_handle_animal')

        # Deleting field 'Character.sk_handle_animal_ranks'
        db.delete_column(u'main_character', 'sk_handle_animal_ranks')

        # Deleting field 'Character.sk_handle_animal_misc'
        db.delete_column(u'main_character', 'sk_handle_animal_misc')

        # Deleting field 'Character.sk_handle_animal_class'
        db.delete_column(u'main_character', 'sk_handle_animal_class')

        # Deleting field 'Character.sk_heal'
        db.delete_column(u'main_character', 'sk_heal')

        # Deleting field 'Character.sk_heal_ranks'
        db.delete_column(u'main_character', 'sk_heal_ranks')

        # Deleting field 'Character.sk_heal_misc'
        db.delete_column(u'main_character', 'sk_heal_misc')

        # Deleting field 'Character.sk_heal_class'
        db.delete_column(u'main_character', 'sk_heal_class')

        # Deleting field 'Character.sk_intimidate'
        db.delete_column(u'main_character', 'sk_intimidate')

        # Deleting field 'Character.sk_intimidate_ranks'
        db.delete_column(u'main_character', 'sk_intimidate_ranks')

        # Deleting field 'Character.sk_intimidate_misc'
        db.delete_column(u'main_character', 'sk_intimidate_misc')

        # Deleting field 'Character.sk_intimidate_class'
        db.delete_column(u'main_character', 'sk_intimidate_class')

        # Deleting field 'Character.sk_knowledge_arcana'
        db.delete_column(u'main_character', 'sk_knowledge_arcana')

        # Deleting field 'Character.sk_knowledge_arcana_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_arcana_ranks')

        # Deleting field 'Character.sk_knowledge_arcana_misc'
        db.delete_column(u'main_character', 'sk_knowledge_arcana_misc')

        # Deleting field 'Character.sk_knowledge_arcana_class'
        db.delete_column(u'main_character', 'sk_knowledge_arcana_class')

        # Deleting field 'Character.sk_knowledge_dungeoneering'
        db.delete_column(u'main_character', 'sk_knowledge_dungeoneering')

        # Deleting field 'Character.sk_knowledge_dungeoneering_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_dungeoneering_ranks')

        # Deleting field 'Character.sk_knowledge_dungeoneering_misc'
        db.delete_column(u'main_character', 'sk_knowledge_dungeoneering_misc')

        # Deleting field 'Character.sk_knowledge_dungeoneering_class'
        db.delete_column(u'main_character', 'sk_knowledge_dungeoneering_class')

        # Deleting field 'Character.sk_knowledge_engineering'
        db.delete_column(u'main_character', 'sk_knowledge_engineering')

        # Deleting field 'Character.sk_knowledge_engineering_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_engineering_ranks')

        # Deleting field 'Character.sk_knowledge_engineering_misc'
        db.delete_column(u'main_character', 'sk_knowledge_engineering_misc')

        # Deleting field 'Character.sk_knowledge_engineering_class'
        db.delete_column(u'main_character', 'sk_knowledge_engineering_class')

        # Deleting field 'Character.sk_knowledge_geography'
        db.delete_column(u'main_character', 'sk_knowledge_geography')

        # Deleting field 'Character.sk_knowledge_geography_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_geography_ranks')

        # Deleting field 'Character.sk_knowledge_geography_misc'
        db.delete_column(u'main_character', 'sk_knowledge_geography_misc')

        # Deleting field 'Character.sk_knowledge_geography_class'
        db.delete_column(u'main_character', 'sk_knowledge_geography_class')

        # Deleting field 'Character.sk_knowledge_history'
        db.delete_column(u'main_character', 'sk_knowledge_history')

        # Deleting field 'Character.sk_knowledge_history_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_history_ranks')

        # Deleting field 'Character.sk_knowledge_history_misc'
        db.delete_column(u'main_character', 'sk_knowledge_history_misc')

        # Deleting field 'Character.sk_knowledge_history_class'
        db.delete_column(u'main_character', 'sk_knowledge_history_class')

        # Deleting field 'Character.sk_knowledge_local'
        db.delete_column(u'main_character', 'sk_knowledge_local')

        # Deleting field 'Character.sk_knowledge_local_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_local_ranks')

        # Deleting field 'Character.sk_knowledge_local_misc'
        db.delete_column(u'main_character', 'sk_knowledge_local_misc')

        # Deleting field 'Character.sk_knowledge_local_class'
        db.delete_column(u'main_character', 'sk_knowledge_local_class')

        # Deleting field 'Character.sk_knowledge_nature'
        db.delete_column(u'main_character', 'sk_knowledge_nature')

        # Deleting field 'Character.sk_knowledge_nature_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_nature_ranks')

        # Deleting field 'Character.sk_knowledge_nature_misc'
        db.delete_column(u'main_character', 'sk_knowledge_nature_misc')

        # Deleting field 'Character.sk_knowledge_nature_class'
        db.delete_column(u'main_character', 'sk_knowledge_nature_class')

        # Deleting field 'Character.sk_knowledge_nobility'
        db.delete_column(u'main_character', 'sk_knowledge_nobility')

        # Deleting field 'Character.sk_knowledge_nobility_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_nobility_ranks')

        # Deleting field 'Character.sk_knowledge_nobility_misc'
        db.delete_column(u'main_character', 'sk_knowledge_nobility_misc')

        # Deleting field 'Character.sk_knowledge_nobility_class'
        db.delete_column(u'main_character', 'sk_knowledge_nobility_class')

        # Deleting field 'Character.sk_knowledge_planes'
        db.delete_column(u'main_character', 'sk_knowledge_planes')

        # Deleting field 'Character.sk_knowledge_planes_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_planes_ranks')

        # Deleting field 'Character.sk_knowledge_planes_misc'
        db.delete_column(u'main_character', 'sk_knowledge_planes_misc')

        # Deleting field 'Character.sk_knowledge_planes_class'
        db.delete_column(u'main_character', 'sk_knowledge_planes_class')

        # Deleting field 'Character.sk_knowledge_religion'
        db.delete_column(u'main_character', 'sk_knowledge_religion')

        # Deleting field 'Character.sk_knowledge_religion_ranks'
        db.delete_column(u'main_character', 'sk_knowledge_religion_ranks')

        # Deleting field 'Character.sk_knowledge_religion_misc'
        db.delete_column(u'main_character', 'sk_knowledge_religion_misc')

        # Deleting field 'Character.sk_knowledge_religion_class'
        db.delete_column(u'main_character', 'sk_knowledge_religion_class')

        # Deleting field 'Character.sk_linguistics'
        db.delete_column(u'main_character', 'sk_linguistics')

        # Deleting field 'Character.sk_linguistics_ranks'
        db.delete_column(u'main_character', 'sk_linguistics_ranks')

        # Deleting field 'Character.sk_linguistics_misc'
        db.delete_column(u'main_character', 'sk_linguistics_misc')

        # Deleting field 'Character.sk_linguistics_class'
        db.delete_column(u'main_character', 'sk_linguistics_class')

        # Deleting field 'Character.sk_perception'
        db.delete_column(u'main_character', 'sk_perception')

        # Deleting field 'Character.sk_perception_ranks'
        db.delete_column(u'main_character', 'sk_perception_ranks')

        # Deleting field 'Character.sk_perception_misc'
        db.delete_column(u'main_character', 'sk_perception_misc')

        # Deleting field 'Character.sk_perform'
        db.delete_column(u'main_character', 'sk_perform')

        # Deleting field 'Character.sk_perform_ranks'
        db.delete_column(u'main_character', 'sk_perform_ranks')

        # Deleting field 'Character.sk_perform_misc'
        db.delete_column(u'main_character', 'sk_perform_misc')

        # Deleting field 'Character.sk_perception_class'
        db.delete_column(u'main_character', 'sk_perception_class')

        # Deleting field 'Character.sk_profession_type'
        db.delete_column(u'main_character', 'sk_profession_type')

        # Deleting field 'Character.sk_profession'
        db.delete_column(u'main_character', 'sk_profession')

        # Deleting field 'Character.sk_profession_ranks'
        db.delete_column(u'main_character', 'sk_profession_ranks')

        # Deleting field 'Character.sk_profession_misc'
        db.delete_column(u'main_character', 'sk_profession_misc')

        # Deleting field 'Character.sk_profession_class'
        db.delete_column(u'main_character', 'sk_profession_class')

        # Deleting field 'Character.sk_ride'
        db.delete_column(u'main_character', 'sk_ride')

        # Deleting field 'Character.sk_ride_ranks'
        db.delete_column(u'main_character', 'sk_ride_ranks')

        # Deleting field 'Character.sk_ride_misc'
        db.delete_column(u'main_character', 'sk_ride_misc')

        # Deleting field 'Character.sk_ride_class'
        db.delete_column(u'main_character', 'sk_ride_class')

        # Deleting field 'Character.sk_sense_motive'
        db.delete_column(u'main_character', 'sk_sense_motive')

        # Deleting field 'Character.sk_sense_motive_ranks'
        db.delete_column(u'main_character', 'sk_sense_motive_ranks')

        # Deleting field 'Character.sk_sense_motive_misc'
        db.delete_column(u'main_character', 'sk_sense_motive_misc')

        # Deleting field 'Character.sk_sense_motive_class'
        db.delete_column(u'main_character', 'sk_sense_motive_class')

        # Deleting field 'Character.sk_sleight_of_hand'
        db.delete_column(u'main_character', 'sk_sleight_of_hand')

        # Deleting field 'Character.sk_sleight_of_hand_ranks'
        db.delete_column(u'main_character', 'sk_sleight_of_hand_ranks')

        # Deleting field 'Character.sk_sleight_of_hand_misc'
        db.delete_column(u'main_character', 'sk_sleight_of_hand_misc')

        # Deleting field 'Character.sk_sleight_of_hand_class'
        db.delete_column(u'main_character', 'sk_sleight_of_hand_class')

        # Deleting field 'Character.sk_spellcraft'
        db.delete_column(u'main_character', 'sk_spellcraft')

        # Deleting field 'Character.sk_spellcraft_ranks'
        db.delete_column(u'main_character', 'sk_spellcraft_ranks')

        # Deleting field 'Character.sk_spellcraft_misc'
        db.delete_column(u'main_character', 'sk_spellcraft_misc')

        # Deleting field 'Character.sk_spellcraft_class'
        db.delete_column(u'main_character', 'sk_spellcraft_class')

        # Deleting field 'Character.sk_stealth'
        db.delete_column(u'main_character', 'sk_stealth')

        # Deleting field 'Character.sk_stealth_ranks'
        db.delete_column(u'main_character', 'sk_stealth_ranks')

        # Deleting field 'Character.sk_steahth_misc'
        db.delete_column(u'main_character', 'sk_steahth_misc')

        # Deleting field 'Character.sk_stealth_class'
        db.delete_column(u'main_character', 'sk_stealth_class')

        # Deleting field 'Character.sk_survival'
        db.delete_column(u'main_character', 'sk_survival')

        # Deleting field 'Character.sk_survival_ranks'
        db.delete_column(u'main_character', 'sk_survival_ranks')

        # Deleting field 'Character.sk_survival_misc'
        db.delete_column(u'main_character', 'sk_survival_misc')

        # Deleting field 'Character.sk_survival_class'
        db.delete_column(u'main_character', 'sk_survival_class')

        # Deleting field 'Character.sk_swim'
        db.delete_column(u'main_character', 'sk_swim')

        # Deleting field 'Character.sk_swim_ranks'
        db.delete_column(u'main_character', 'sk_swim_ranks')

        # Deleting field 'Character.sk_swim_misc'
        db.delete_column(u'main_character', 'sk_swim_misc')

        # Deleting field 'Character.sk_swim_class'
        db.delete_column(u'main_character', 'sk_swim_class')

        # Deleting field 'Character.sk_use_magical_device'
        db.delete_column(u'main_character', 'sk_use_magical_device')

        # Deleting field 'Character.sk_use_magical_device_ranks'
        db.delete_column(u'main_character', 'sk_use_magical_device_ranks')

        # Deleting field 'Character.sk_use_magical_device_misc'
        db.delete_column(u'main_character', 'sk_use_magical_device_misc')

        # Deleting field 'Character.sk_use_magical_device_class'
        db.delete_column(u'main_character', 'sk_use_magical_device_class')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.character': {
            'Meta': {'object_name': 'Character'},
            'ability_cha': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_cha_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_cha_temp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_con': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_con_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_con_temp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_dex': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_dex_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_dex_temp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_int': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_int_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_int_temp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_str': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_str_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_str_temp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_wis': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_wis_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_wis_temp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_armor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_natural': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_shield': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'bab': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_class_1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'cmb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'current_game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Game']", 'null': 'True', 'blank': 'True'}),
            'current_hp': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'deity': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'eyes': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'hair': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hp': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiative': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'initiative_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'race': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'sk_acrobatics': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_acrobatics_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_acrobatics_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_acrobatics_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_appraise': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_appraise_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_appraise_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_appraise_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_bluff': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_bluff_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_bluff_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_bluff_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_climb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_climb_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_climb_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_climb_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_craft': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_craft_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_craft_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_craft_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_craft_type': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'sk_diplomacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_diplomacy_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_diplomacy_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_diplomacy_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_disable_device_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_disable_device_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_disable_device_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_disable_devie': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_disguise': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_disguise_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_disguise_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_disguise_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_escape_artist': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_escape_artist_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_escape_artist_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_escape_artist_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_fly': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_fly_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_fly_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_fly_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_handle_animal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_handle_animal_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_handle_animal_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_handle_animal_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_heal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_heal_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_heal_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_heal_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_intimidate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_intimidate_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_intimidate_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_intimidate_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_arcana': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_arcana_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_arcana_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_arcana_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_dungeoneering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_dungeoneering_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_dungeoneering_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_dungeoneering_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_engineering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_engineering_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_engineering_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_engineering_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_geography': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_geography_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_geography_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_geography_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_history': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_history_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_history_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_history_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_local': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_local_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_local_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_local_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_nature': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_nature_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_nature_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_nature_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_nobility': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_nobility_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_nobility_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_nobility_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_planes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_planes_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_planes_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_planes_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_religion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_religion_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_knowledge_religion_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_knowledge_religion_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_linguistics': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_linguistics_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_linguistics_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_linguistics_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_perception_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_perception_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_perception_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_perform': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_perform_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_perform_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_profession': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_profession_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_profession_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_profession_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_profession_type': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'sk_ride': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_ride_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_ride_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_ride_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_sense_motive': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_sense_motive_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_sense_motive_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_sense_motive_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_sleight_of_hand': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_sleight_of_hand_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_sleight_of_hand_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_sleight_of_hand_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_spellcraft': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_spellcraft_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_spellcraft_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_spellcraft_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_steahth_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_stealth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_stealth_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_stealth_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_survival': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_survival_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_survival_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_survival_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_swim': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_swim_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_swim_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_swim_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_use_magical_device': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_use_magical_device_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_use_magical_device_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_use_magical_device_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'speed_armor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_climb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_fly': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_normal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_swim': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spell_resistance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'main.game': {
            'Meta': {'object_name': 'Game'},
            'gm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['main']