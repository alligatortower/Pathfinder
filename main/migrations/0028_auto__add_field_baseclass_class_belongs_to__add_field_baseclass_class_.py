# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BaseClass.class_belongs_to'
        db.add_column(u'main_baseclass', 'class_belongs_to',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['main.Character'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'BaseClass.class_is_favored'
        db.add_column(u'main_baseclass', 'class_is_favored',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BaseClass.class_base_attack_bonus_1'
        db.add_column(u'main_baseclass', 'class_base_attack_bonus_1',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'BaseClass.class_base_attack_bonus_2'
        db.add_column(u'main_baseclass', 'class_base_attack_bonus_2',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'BaseClass.class_base_attack_bonus_3'
        db.add_column(u'main_baseclass', 'class_base_attack_bonus_3',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'BaseClass.class_base_attack_bonus_4'
        db.add_column(u'main_baseclass', 'class_base_attack_bonus_4',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'BaseClass.class_base_fortitude_save'
        db.add_column(u'main_baseclass', 'class_base_fortitude_save',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'BaseClass.class_base_reflex_save'
        db.add_column(u'main_baseclass', 'class_base_reflex_save',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'BaseClass.class_base_willpower_save'
        db.add_column(u'main_baseclass', 'class_base_willpower_save',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BaseClass.class_belongs_to'
        db.delete_column(u'main_baseclass', 'class_belongs_to_id')

        # Deleting field 'BaseClass.class_is_favored'
        db.delete_column(u'main_baseclass', 'class_is_favored')

        # Deleting field 'BaseClass.class_base_attack_bonus_1'
        db.delete_column(u'main_baseclass', 'class_base_attack_bonus_1')

        # Deleting field 'BaseClass.class_base_attack_bonus_2'
        db.delete_column(u'main_baseclass', 'class_base_attack_bonus_2')

        # Deleting field 'BaseClass.class_base_attack_bonus_3'
        db.delete_column(u'main_baseclass', 'class_base_attack_bonus_3')

        # Deleting field 'BaseClass.class_base_attack_bonus_4'
        db.delete_column(u'main_baseclass', 'class_base_attack_bonus_4')

        # Deleting field 'BaseClass.class_base_fortitude_save'
        db.delete_column(u'main_baseclass', 'class_base_fortitude_save')

        # Deleting field 'BaseClass.class_base_reflex_save'
        db.delete_column(u'main_baseclass', 'class_base_reflex_save')

        # Deleting field 'BaseClass.class_base_willpower_save'
        db.delete_column(u'main_baseclass', 'class_base_willpower_save')


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
        u'main.armor': {
            'Meta': {'object_name': 'Armor', '_ormbases': [u'main.Equipment']},
            'ac_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'armor_check_penalty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Equipment']", 'unique': 'True', 'primary_key': 'True'}),
            'max_dex': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'speed_if_base_20': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_if_base_30': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spell_fail_chance': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'main.baseclass': {
            'Meta': {'object_name': 'BaseClass'},
            'class_base_attack_bonus_1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_base_attack_bonus_2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_base_attack_bonus_3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_base_attack_bonus_4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_base_fortitude_save': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_base_reflex_save': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_base_willpower_save': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_belongs_to': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['main.Character']", 'null': 'True', 'blank': 'True'}),
            'class_is_favored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'class_levels': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '30'}),
            'class_name': ('django.db.models.fields.CharField', [], {'default': "'Barbarian'", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.character': {
            'Meta': {'object_name': 'Character'},
            'ability_cha_base': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'ability_cha_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_cha_score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_cha_temp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_con_base': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'ability_con_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_con_score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_con_temp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_dex_base': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10', 'db_column': "'ability_dex'"}),
            'ability_dex_mod': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'ability_dex_mod'"}),
            'ability_dex_score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_dex_temp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_int_base': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'ability_int_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_int_score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_int_temp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_str_base': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'ability_str_mod': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'ability_str_mod'"}),
            'ability_str_score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_str_temp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_wis_base': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'ability_wis_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ability_wis_score': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ability_wis_temp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ac_armor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_armor_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_deflection': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_dodge': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_ff_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_misc_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_natural': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_shield': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ac_touch_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'armor_check_penalty': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'base_attack_bonus_1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_attack_bonus_2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_attack_bonus_3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_attack_bonus_4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_attack_bonus_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'combat_maneuver_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'combat_maneuver_bonus_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'combat_maneuver_defense': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'combat_maneuver_defense_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'current_game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Game']", 'null': 'True', 'blank': 'True'}),
            'current_hp': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'deity': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'discription': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '1000'}),
            'eyes': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'fortitude_save_base': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fortitude_save_equip': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fortitude_save_feat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fortitude_save_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fortitude_save_misc_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fortitude_save_racial': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fortitude_save_temp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fortitude_save_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'hair': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'hd': ('django.db.models.fields.CharField', [], {'default': "'1d6'", 'max_length': '10'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiative_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'initiative_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'max_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'melee_attack_bonus_1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'melee_attack_bonus_2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'melee_attack_bonus_3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'melee_attack_bonus_4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'melee_attack_bonus_str_or_dex': ('django.db.models.fields.CharField', [], {'default': "'str'", 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'nonlethal_damage': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'race': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '20'}),
            'ranged_attack_bonus_1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ranged_attack_bonus_2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ranged_attack_bonus_3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ranged_attack_bonus_4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reflex_save_base': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reflex_save_equip': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reflex_save_feat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reflex_save_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reflex_save_misc_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reflex_save_racial': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reflex_save_temp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reflex_save_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'Medium'", 'max_length': '20'}),
            'size_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_acrobatics': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'sk_acrobatics'"}),
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
            'sk_diplomacy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_diplomacy_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_diplomacy_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_diplomacy_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_disable_device': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_disable_device_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_disable_device_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_disable_device_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'sk_perform_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_perform_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_perform_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'sk_stealth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_stealth_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_stealth_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'speed_base': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_climb': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_fly': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_swim': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spell_resistance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_hp': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'total_levels': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpower_save_base': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpower_save_equip': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpower_save_feat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpower_save_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpower_save_misc_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpower_save_racial': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpower_save_temp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpower_save_total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'main.equipment': {
            'Meta': {'object_name': 'Equipment', '_ormbases': [u'main.Item']},
            'is_a': ('django.db.models.fields.CharField', [], {'default': "'Weapon'", 'max_length': '10'}),
            'is_equipped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'proficiency': ('django.db.models.fields.CharField', [], {'default': "'Light'", 'max_length': '10'}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'medium'", 'max_length': '10'})
        },
        u'main.game': {
            'Meta': {'object_name': 'Game'},
            'gm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'main.item': {
            'Meta': {'object_name': 'Item'},
            'cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'current_game': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['main.Game']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'---'", 'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'default': "'metal'", 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Equipment'", 'max_length': '256'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['main.Character']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'main.multiskill': {
            'Meta': {'unique_together': "(('character', 'sk_domain'),)", 'object_name': 'MultiSkill'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sk_class': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_craft_or_profession': ('django.db.models.fields.CharField', [], {'default': "'craft'", 'max_length': '10'}),
            'sk_domain': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sk_misc': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_ranks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'main.weapon': {
            'Meta': {'object_name': 'Weapon', '_ormbases': [u'main.Equipment']},
            'attack_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'crit_muliplier': ('django.db.models.fields.CharField', [], {'default': "'x2'", 'max_length': '3'}),
            'crit_range': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'damage': ('django.db.models.fields.CharField', [], {'default': "'1d3'", 'max_length': '10'}),
            'damage_type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '10'}),
            u'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Equipment']", 'unique': 'True', 'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'range_increment': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reach': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weapon_type': ('django.db.models.fields.CharField', [], {'default': "'simple'", 'max_length': '20'})
        }
    }

    complete_apps = ['main']