import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from resources.datatables import FactionStatus
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('corvette_rebel_commandant')
	mobileTemplate.setLevel(82)
	mobileTemplate.setDifficulty(Difficulty.ELITE)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("rebel")
	mobileTemplate.setAssistRange(6)
	mobileTemplate.setStalker(False)
	mobileTemplate.setFaction("rebel")
	mobileTemplate.setFactionStatus(FactionStatus.Combatant)
	mobileTemplate.setOptionsBitmask(Options.ATTACKABLE)
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_rebel_brigadier_general_bith_male.iff')
	templates.add('object/mobile/shared_dressed_rebel_brigadier_general_human_female_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_brigadier_general_moncal_female.iff')
	templates.add('object/mobile/shared_dressed_rebel_brigadier_general_rodian_female_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_brigadier_general_sullustan_male.iff')
	templates.add('object/mobile/shared_dressed_rebel_brigadier_general_trandoshan_female.iff')				
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/ranged/pistol/shared_pistol_alliance_disruptor.iff', WeaponType.PISTOL, 1.0, 15, 'energy')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('rangedShot')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('rebel_commandant', mobileTemplate)
	return