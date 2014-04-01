import sys

def setup(core, object):
	object.setStfFilename('static_item_n')
	object.setStfName('item_jedi_robe_light_04_04')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_jedi_robe_light_04_04')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:constitution_modified', 185)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:strength_modified', 185)
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:agility_modified', 185)
	object.setStringAttribute('protection_level', 'Luminous')
	object.setStringAttribute('class_required', 'Jedi')
	object.setIntAttribute('required_combat_level', 80)
	object.setAttachment('type', 'jedi_robe')
	object.setStringAttribute('@set_bonus:piece_bonus_count_2', '@set_bonus:set_bonus_jedi_robe_1')
	return
