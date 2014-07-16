import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('jabbas_palace_fnast_drexler')
	mobileTemplate.setLevel(18)
	mobileTemplate.setDifficulty(Difficulty.ELITE)

	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("jabba")
	mobileTemplate.setAssistRange(6)
	mobileTemplate.setStalker(False)	
	mobileTemplate.setOptionsBitmask(Options.ATTACKABLE)
	
	templates = Vector()

	templates.add('object/mobile/shared_fnast_drexler.iff')
	mobileTemplate.setTemplates(templates)

	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', WeaponType.UNARMED, 1.0, 6, 'kinetic')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('MeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('jabbas_palace_fnast_drexler', mobileTemplate)
	return