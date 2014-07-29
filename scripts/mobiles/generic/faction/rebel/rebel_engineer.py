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
	
	mobileTemplate.setCreatureName('corvette_rebel_engineer')
	mobileTemplate.setLevel(80)
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
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_female_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_female_02.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_male_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_male_02.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_male_03.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_male_04.iff')				
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/ranged/rifle/shared_rifle_dlt20a.iff', WeaponType.RIFLE, 1.0, 24, 'energy')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('rangedShot')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('rebel_engineer', mobileTemplate)
	return