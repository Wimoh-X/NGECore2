import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('borgle_harvester')
	mobileTemplate.setLevel(37)
	mobileTemplate.setMinLevel(37)
	mobileTemplate.setMaxLevel(37)
	mobileTemplate.setDifficulty(0)
	mobileTemplate.setAttackRange(5)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(6)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Carnivore Meat")
	mobileTemplate.setMeatAmount(5)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setHideAmount(5)
	mobileTemplate.setBoneType("Avian Bones")
	mobileTemplate.setBoneAmount(5)
	mobileTemplate.setSocialGroup("borgle")
	mobileTemplate.setAssistRange(0)
	mobileTemplate.setStalker(False)
	mobileTemplate.setOptionsBitmask(128)
	
	templates = Vector()
	templates.add('object/mobile/shared_borgle.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', 6, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('borgle_harvester', mobileTemplate)
	return