from os import system
import platform

if platform.system() == "Windows": clear = "cls"
else: clear = "clear"

###########################################################
# DATA

humeJobs = [dict() for i in range(16)]
humeJobs[0] = {"Name": "soldier", "BaseHP": 90, "BaseMP": 15, "BaseSpd": 57, "BaseAtk": 88, "BaseDef": 84, "BaseMgk": 60, "BaseRes": 72, "HPGrowth": 8, "MPGrowth": 1, "SpdGrowth": 0.5, "AtkGrowth": 9, "DefGrowth": 8, "MgkGrowth": 6, "ResGrowth": 7}
humeJobs[1] = {"Name": "thief", "BaseHP": 83, "BaseMP": 15, "BaseSpd": 60, "BaseAtk": 76, "BaseDef": 74, "BaseMgk": 76, "BaseRes": 64, "HPGrowth": 6, "MPGrowth": 1, "SpdGrowth": 0.7, "AtkGrowth": 7, "DefGrowth": 7, "MgkGrowth": 7, "ResGrowth": 6}
humeJobs[2] = {"Name": "white mage", "BaseHP": 84, "BaseMP": 36, "BaseSpd": 58, "BaseAtk": 64, "BaseDef": 73, "BaseMgk": 84, "BaseRes": 80, "HPGrowth": 6, "MPGrowth": 4, "SpdGrowth": 0.52, "AtkGrowth": 6, "DefGrowth": 7, "MgkGrowth": 8, "ResGrowth": 8}
humeJobs[3] = {"Name": "black mage", "BaseHP": 79, "BaseMP": 38, "BaseSpd": 56, "BaseAtk": 60, "BaseDef": 68, "BaseMgk": 91, "BaseRes": 96, "HPGrowth": 5, "MPGrowth": 5, "SpdGrowth": 0.46, "AtkGrowth": 6, "DefGrowth": 6, "MgkGrowth": 10, "ResGrowth": 10}
humeJobs[4] = {"Name": "archer", "BaseHP": 86, "BaseMP": 18, "BaseSpd": 59, "BaseAtk": 72, "BaseDef": 72, "BaseMgk": 64, "BaseRes": 79, "HPGrowth": 7, "MPGrowth": 1, "SpdGrowth": 0.55, "AtkGrowth": 7, "DefGrowth": 7, "MgkGrowth": 6, "ResGrowth": 7}
humeJobs[5] = {"Name": "paladin", "BaseHP": 88, "BaseMP": 22, "BaseSpd": 56, "BaseAtk": 80, "BaseDef": 92, "BaseMgk": 72, "BaseRes": 88, "HPGrowth": 7, "MPGrowth": 2, "SpdGrowth": 0.48, "AtkGrowth": 8, "DefGrowth": 10, "MgkGrowth": 7, "ResGrowth": 9}
humeJobs[6] = {"Name": "fighter", "BaseHP": 84, "BaseMP": 12, "BaseSpd": 58, "BaseAtk": 92, "BaseDef": 86, "BaseMgk": 56, "BaseRes": 68, "HPGrowth": 6, "MPGrowth": 1, "SpdGrowth": 0.53, "AtkGrowth": 10, "DefGrowth": 8, "MgkGrowth": 5, "ResGrowth": 6}
humeJobs[7] = {"Name": "parivir", "BaseHP": 86, "BaseMP": 10, "BaseSpd": 60, "BaseAtk": 93, "BaseDef": 69, "BaseMgk": 68, "BaseRes": 69, "HPGrowth": 7, "MPGrowth": 1, "SpdGrowth": 0.62, "AtkGrowth": 11, "DefGrowth": 7, "MgkGrowth": 6, "ResGrowth": 5}
humeJobs[8] = {"Name": "ninja", "BaseHP": 79, "BaseMP": 21, "BaseSpd": 65, "BaseAtk": 88, "BaseDef": 68, "BaseMgk": 78, "BaseRes": 76, "HPGrowth": 5, "MPGrowth": 2, "SpdGrowth": 0.9, "AtkGrowth": 9, "DefGrowth": 6, "MgkGrowth": 7, "ResGrowth": 7}
humeJobs[9] = {"Name": "illusionist", "BaseHP": 76, "BaseMP": 38, "BaseSpd": 54, "BaseAtk": 60, "BaseDef": 64, "BaseMgk": 92, "BaseRes": 84, "HPGrowth": 5, "MPGrowth": 7, "SpdGrowth": 0.35, "AtkGrowth": 6, "DefGrowth": 6, "MgkGrowth": 9, "ResGrowth": 8}
humeJobs[10] = {"Name": "blue mage", "BaseHP": 84, "BaseMP": 30, "BaseSpd": 57, "BaseAtk": 80, "BaseDef": 88, "BaseMgk": 84, "BaseRes": 92, "HPGrowth": 6, "MPGrowth": 3, "SpdGrowth": 0.5, "AtkGrowth": 8, "DefGrowth": 9, "MgkGrowth": 8, "ResGrowth": 9}
humeJobs[11] = {"Name": "hunter", "BaseHP": 84, "BaseMP": 26, "BaseSpd": 61, "BaseAtk": 84, "BaseDef": 66, "BaseMgk": 68, "BaseRes": 84, "HPGrowth": 6, "MPGrowth": 3, "SpdGrowth": 0.65, "AtkGrowth": 8, "DefGrowth": 6, "MgkGrowth": 7, "ResGrowth": 8}
humeJobs[12] = {"Name": "seer", "BaseHP": 83, "BaseMP": 42, "BaseSpd": 55, "BaseAtk": 63, "BaseDef": 71, "BaseMgk": 90, "BaseRes": 99, "HPGrowth": 6, "MPGrowth": 7, "SpdGrowth": 0.4, "AtkGrowth": 6, "DefGrowth": 7, "MgkGrowth": 8, "ResGrowth": 11}
humeJobs[13] = {"Name": "sky pirate", "BaseHP": 85, "BaseMP": 14, "BaseSpd": 60, "BaseAtk": 76, "BaseDef": 74, "BaseMgk": 76, "BaseRes": 72, "HPGrowth": 6, "MPGrowth": 2, "SpdGrowth": 0.64, "AtkGrowth": 7, "DefGrowth": 7, "MgkGrowth": 7, "ResGrowth": 7}
humeJobs[14] = {"Name": "heritor", "BaseHP": 84, "BaseMP": 36, "BaseSpd": 61, "BaseAtk": 80, "BaseDef": 86, "BaseMgk": 84, "BaseRes": 80, "HPGrowth": 6, "MPGrowth": 4, "SpdGrowth": 0.62, "AtkGrowth": 8, "DefGrowth": 8, "MgkGrowth": 8, "ResGrowth": 8}
humeJobs[15] = {"Name": "agent", "BaseHP": 86, "BaseMP": 12, "BaseSpd": 59, "BaseAtk": 80, "BaseDef": 83, "BaseMgk": 70, "BaseRes": 72, "HPGrowth": 7, "MPGrowth": 2, "SpdGrowth": 0.54, "AtkGrowth": 8, "DefGrowth": 8, "MgkGrowth": 6, "ResGrowth": 7}

vieraJobs = [dict() for i in range(11)]
vieraJobs[0] = {"Name": "fencer", "BaseHP": 89, "BaseMP": 15, "BaseSpd": 61, "BaseAtk": 90, "BaseDef": 78, "BaseMgk": 69, "BaseRes": 64, "HPGrowth": 8, "MPGrowth": 1, "SpdGrowth": 0.69, "AtkGrowth": 10, "DefGrowth": 7, "MgkGrowth": 6, "ResGrowth": 6}
vieraJobs[1] = {"Name": "white mage", "BaseHP": 81, "BaseMP": 36, "BaseSpd": 59, "BaseAtk": 63, "BaseDef": 72, "BaseMgk": 84, "BaseRes": 80, "HPGrowth": 6, "MPGrowth": 5, "SpdGrowth": 0.58, "AtkGrowth": 6, "DefGrowth": 7, "MgkGrowth": 8, "ResGrowth": 8}
vieraJobs[2] = {"Name": "green mage", "BaseHP": 85, "BaseMP": 30, "BaseSpd": 62, "BaseAtk": 73, "BaseDef": 76, "BaseMgk": 84, "BaseRes": 79, "HPGrowth": 6, "MPGrowth": 3, "SpdGrowth": 0.86, "AtkGrowth": 7, "DefGrowth": 7, "MgkGrowth": 8, "ResGrowth": 7}
vieraJobs[3] = {"Name": "archer", "BaseHP": 86, "BaseMP": 19, "BaseSpd": 61, "BaseAtk": 75, "BaseDef": 71, "BaseMgk": 70, "BaseRes": 70, "HPGrowth": 7, "MPGrowth": 1, "SpdGrowth": 0.66, "AtkGrowth": 8, "DefGrowth": 7, "MgkGrowth": 6, "ResGrowth": 7}
vieraJobs[4] = {"Name": "elementalist", "BaseHP": 80, "BaseMP": 28, "BaseSpd": 57, "BaseAtk": 70, "BaseDef": 74, "BaseMgk": 88, "BaseRes": 73, "HPGrowth": 6, "MPGrowth": 3, "SpdGrowth": 0.41, "AtkGrowth": 7, "DefGrowth": 7, "MgkGrowth": 10, "ResGrowth": 7}
vieraJobs[5] = {"Name": "red mage", "BaseHP": 83, "BaseMP": 28, "BaseSpd": 60, "BaseAtk": 82, "BaseDef": 63, "BaseMgk": 86, "BaseRes": 70, "HPGrowth": 6, "MPGrowth": 2, "SpdGrowth": 0.62, "AtkGrowth": 9, "DefGrowth": 6, "MgkGrowth": 9, "ResGrowth": 6}
vieraJobs[6] = {"Name": "spellblade", "BaseHP": 80, "BaseMP": 24, "BaseSpd": 60, "BaseAtk": 85, "BaseDef": 80, "BaseMgk": 76, "BaseRes": 75, "HPGrowth": 5, "MPGrowth": 2, "SpdGrowth": 0.64, "AtkGrowth": 9, "DefGrowth": 7, "MgkGrowth": 7, "ResGrowth": 7}
vieraJobs[7] = {"Name": "summoner", "BaseHP": 74, "BaseMP": 42, "BaseSpd": 58, "BaseAtk": 59, "BaseDef": 61, "BaseMgk": 90, "BaseRes": 74, "HPGrowth": 5, "MPGrowth": 4, "SpdGrowth": 0.56, "AtkGrowth": 6, "DefGrowth": 6, "MgkGrowth": 11, "ResGrowth": 8}
vieraJobs[8] = {"Name": "assassin", "BaseHP": 76, "BaseMP": 16, "BaseSpd": 65, "BaseAtk": 77, "BaseDef": 68, "BaseMgk": 71, "BaseRes": 66, "HPGrowth": 5, "MPGrowth": 1, "SpdGrowth": 0.96, "AtkGrowth": 8, "DefGrowth": 6, "MgkGrowth": 7, "ResGrowth": 6}
vieraJobs[9] = {"Name": "sniper", "BaseHP": 80, "BaseMP": 18, "BaseSpd": 58, "BaseAtk": 93, "BaseDef": 65, "BaseMgk": 73, "BaseRes": 72, "HPGrowth": 6, "MPGrowth": 1, "SpdGrowth": 0.59, "AtkGrowth": 11, "DefGrowth": 6, "MgkGrowth": 7, "ResGrowth": 7}
vieraJobs[10] = {"Name": "dancer", "BaseHP": 78, "BaseMP": 48, "BaseSpd": 58, "BaseAtk": 64, "BaseDef": 60, "BaseMgk": 87, "BaseRes": 80, "HPGrowth": 6, "MPGrowth": 6, "SpdGrowth": 0.58, "AtkGrowth": 6, "DefGrowth": 6, "MgkGrowth": 8, "ResGrowth": 8}

bangaaJobs = [dict for i in range(10)]
bangaaJobs[0] = {"Name": "warrior", "BaseHP": 96, "BaseMP": 10, "BaseSpd": 57, "BaseAtk": 87, "BaseDef": 88, "BaseMgk": 58, "BaseRes": 66, "HPGrowth": 9, "MPGrowth": 2, "SpdGrowth": 0.5, "AtkGrowth": 9, "DefGrowth": 8, "MgkGrowth": 6, "ResGrowth": 6}
bangaaJobs[1] = {"Name": "white monk", "BaseHP": 82, "BaseMP": 12, "BaseSpd": 60, "BaseAtk": 89, "BaseDef": 70, "BaseMgk": 70, "BaseRes": 68, "HPGrowth": 6, "MPGrowth": 2, "SpdGrowth": 0.61, "AtkGrowth": 9, "DefGrowth": 7, "MgkGrowth": 7, "ResGrowth": 6}
bangaaJobs[2] = {"Name": "dragoon", "BaseHP": 90, "BaseMP": 6, "BaseSpd": 60, "BaseAtk": 97, "BaseDef": 90, "BaseMgk": 53, "BaseRes": 62, "HPGrowth": 8, "MPGrowth": 1, "SpdGrowth": 0.62, "AtkGrowth": 11, "DefGrowth": 9, "MgkGrowth": 5, "ResGrowth": 5}
bangaaJobs[3] = {"Name": "defender", "BaseHP": 90, "BaseMP": 8, "BaseSpd": 56, "BaseAtk": 84, "BaseDef": 98, "BaseMgk": 60, "BaseRes": 78, "HPGrowth": 8, "MPGrowth": 1, "SpdGrowth": 0.45, "AtkGrowth": 8, "DefGrowth": 11, "MgkGrowth": 6, "ResGrowth": 7}
bangaaJobs[4] = {"Name": "gladiator", "BaseHP": 92, "BaseMP": 18, "BaseSpd": 58, "BaseAtk": 99, "BaseDef": 90, "BaseMgk": 57, "BaseRes": 64, "HPGrowth": 8, "MPGrowth": 2, "SpdGrowth": 0.55, "AtkGrowth": 12, "DefGrowth": 8, "MgkGrowth": 6, "ResGrowth": 6}
bangaaJobs[5] = {"Name": "master monk", "BaseHP": 81, "BaseMP": 14, "BaseSpd": 61, "BaseAtk": 95, "BaseDef": 78, "BaseMgk": 76, "BaseRes": 76, "HPGrowth": 6, "MPGrowth": 3, "SpdGrowth": 0.71, "AtkGrowth": 11, "DefGrowth": 8, "MgkGrowth": 8, "ResGrowth": 7}
bangaaJobs[6] = {"Name": "bishop", "BaseHP": 80, "BaseMP": 28, "BaseSpd": 55, "BaseAtk": 65, "BaseDef": 69, "BaseMgk": 82, "BaseRes": 86, "HPGrowth": 6, "MPGrowth": 5, "SpdGrowth": 0.39, "AtkGrowth": 6, "DefGrowth": 6, "MgkGrowth": 9, "ResGrowth": 8}
bangaaJobs[7] = {"Name": "templar", "BaseHP": 92, "BaseMP": 20, "BaseSpd": 53, "BaseAtk": 86, "BaseDef": 94, "BaseMgk": 75, "BaseRes": 80, "HPGrowth": 7, "MPGrowth": 3, "SpdGrowth": 0.34, "AtkGrowth": 9, "DefGrowth": 10, "MgkGrowth": 7, "ResGrowth": 7}
bangaaJobs[8] = {"Name": "cannoneer", "BaseHP": 85, "BaseMP": 19, "BaseSpd": 59, "BaseAtk": 76, "BaseDef": 71, "BaseMgk": 65, "BaseRes": 72, "HPGrowth": 7, "MPGrowth": 3, "SpdGrowth": 0.57, "AtkGrowth": 7, "DefGrowth": 7, "MgkGrowth": 7, "ResGrowth": 7}
bangaaJobs[9] = {"Name": "trickster", "BaseHP": 80, "BaseMP": 7, "BaseSpd": 64, "BaseAtk": 71, "BaseDef": 73, "BaseMgk": 89, "BaseRes": 74, "HPGrowth": 5, "MPGrowth": 1, "SpdGrowth": 0.88, "AtkGrowth": 7, "DefGrowth": 7, "MgkGrowth": 10, "ResGrowth": 7}

nuMouJobs = [dict for i in range(9)]
nuMouJobs[0] = {"Name": "white mage", "BaseHP": 79, "BaseMP": 36, "BaseSpd": 58, "BaseAtk": 64, "BaseDef": 73, "BaseMgk": 84, "BaseRes": 80, "HPGrowth": 5, "MPGrowth": 6, "SpdGrowth": 0.52, "AtkGrowth": 6, "DefGrowth": 7, "MgkGrowth": 8, "ResGrowth": 9}
nuMouJobs[1] = {"Name": "black mage", "BaseHP": 77, "BaseMP": 34, "BaseSpd": 56, "BaseAtk": 60, "BaseDef": 68, "BaseMgk": 91, "BaseRes": 96, "HPGrowth": 5, "MPGrowth": 6, "SpdGrowth": 0.46, "AtkGrowth": 6, "DefGrowth": 6, "MgkGrowth": 11, "ResGrowth": 10}
nuMouJobs[2] = {"Name": "beastmaster", "BaseHP": 88, "BaseMP": 19, "BaseSpd": 59, "BaseAtk": 91, "BaseDef": 86, "BaseMgk": 69, "BaseRes": 72, "HPGrowth": 7, "MPGrowth": 2, "SpdGrowth": 0.60, "AtkGrowth": 10, "DefGrowth": 8, "MgkGrowth": 6, "ResGrowth": 7}
nuMouJobs[3] = {"Name": "time mage", "BaseHP": 78, "BaseMP": 38, "BaseSpd": 57, "BaseAtk": 59, "BaseDef": 61, "BaseMgk": 89, "BaseRes": 96, "HPGrowth": 5, "MPGrowth": 6, "SpdGrowth": 0.50, "AtkGrowth": 5, "DefGrowth": 6, "MgkGrowth": 10, "ResGrowth": 10}
nuMouJobs[4] = {"Name": "illusionist", "BaseHP": 76, "BaseMP": 42, "BaseSpd": 54, "BaseAtk": 60, "BaseDef": 63, "BaseMgk": 92, "BaseRes": 84, "HPGrowth": 5, "MPGrowth": 7, "SpdGrowth": 0.35, "AtkGrowth": 6, "DefGrowth": 6, "MgkGrowth": 9, "ResGrowth": 9}
nuMouJobs[5] = {"Name": "alchemist", "BaseHP": 81, "BaseMP": 44, "BaseSpd": 58, "BaseAtk": 71, "BaseDef": 64, "BaseMgk": 90, "BaseRes": 99, "HPGrowth": 6, "MPGrowth": 7, "SpdGrowth": 0.54, "AtkGrowth": 7, "DefGrowth": 6, "MgkGrowth": 10, "ResGrowth": 11}
nuMouJobs[6] = {"Name": "arcanist", "BaseHP": 74, "BaseMP": 48, "BaseSpd": 53, "BaseAtk": 59, "BaseDef": 60, "BaseMgk": 87, "BaseRes": 74, "HPGrowth": 5, "MPGrowth": 8, "SpdGrowth": 0.34, "AtkGrowth": 5, "DefGrowth": 6, "MgkGrowth": 8, "ResGrowth": 7}
nuMouJobs[7] = {"Name": "sage", "BaseHP": 84, "BaseMP": 32, "BaseSpd": 56, "BaseAtk": 79, "BaseDef": 73, "BaseMgk": 89, "BaseRes": 7, "HPGrowth": 7, "MPGrowth": 4, "SpdGrowth": 0.48, "AtkGrowth": 8, "DefGrowth": 7, "MgkGrowth": 9, "ResGrowth": 8}
nuMouJobs[8] = {"Name": "scholar", "BaseHP": 85, "BaseMP": 24, "BaseSpd": 58, "BaseAtk": 88, "BaseDef": 77, "BaseMgk": 78, "BaseRes": 71, "HPGrowth": 7, "MPGrowth": 3, "SpdGrowth": 0.58, "AtkGrowth": 10, "DefGrowth": 7, "MgkGrowth": 7, "ResGrowth": 7}

moogleJobs = [dict for i in range(11)]
moogleJobs[0] = {"Name": "animist", "BaseHP": 85, "BaseMP": 22, "BaseSpd": 60, "BaseAtk": 81, "BaseDef": 88, "BaseMgk": 70, "BaseRes": 80, "HPGrowth": 7, "MPGrowth": 2, "SpdGrowth": 0.56, "AtkGrowth": 8, "DefGrowth": 9, "MgkGrowth": 7, "ResGrowth": 8}
moogleJobs[1] = {"Name": "thief", "BaseHP": 83, "BaseMP": 15, "BaseSpd": 62, "BaseAtk": 76, "BaseDef": 74, "BaseMgk": 76, "BaseRes": 64, "HPGrowth": 6, "MPGrowth": 1, "SpdGrowth": 0.70, "AtkGrowth": 7, "DefGrowth": 7, "MgkGrowth": 7, "ResGrowth": 6}
moogleJobs[2] = {"Name": "black mage", "BaseHP": 77, "BaseMP": 34, "BaseSpd": 56, "BaseAtk": 60, "BaseDef": 68, "BaseMgk": 91, "BaseRes": 96, "HPGrowth": 5, "MPGrowth": 6, "SpdGrowth": 0.46, "AtkGrowth": 6, "DefGrowth": 6, "MgkGrowth": 10, "ResGrowth": 10}
moogleJobs[3] = {"Name": "moogle knight", "BaseHP": 88, "BaseMP": 28, "BaseSpd": 56, "BaseAtk": 88, "BaseDef": 91, "BaseMgk": 72, "BaseRes": 84, "HPGrowth": 7, "MPGrowth": 3, "SpdGrowth": 0.48, "AtkGrowth": 10, "DefGrowth": 11, "MgkGrowth": 6, "ResGrowth": 9}
moogleJobs[4] = {"Name": "fusilier", "BaseHP": 85, "BaseMP": 12, "BaseSpd": 59, "BaseAtk": 80, "BaseDef": 83, "BaseMgk": 70, "BaseRes": 72, "HPGrowth": 6, "MPGrowth": 1, "SpdGrowth": 0.54, "AtkGrowth": 8, "DefGrowth": 8, "MgkGrowth": 6, "ResGrowth": 7}
moogleJobs[5] = {"Name": "juggler", "BaseHP": 81, "BaseMP": 18, "BaseSpd": 64, "BaseAtk": 82, "BaseDef": 84, "BaseMgk": 72, "BaseRes": 68, "HPGrowth": 6, "MPGrowth": 1, "SpdGrowth": 0.74, "AtkGrowth": 9, "DefGrowth": 9, "MgkGrowth": 7, "ResGrowth": 6}
moogleJobs[6] = {"Name": "tinker", "BaseHP": 82, "BaseMP": 24, "BaseSpd": 55, "BaseAtk": 84, "BaseDef": 86, "BaseMgk": 82, "BaseRes": 98, "HPGrowth": 7, "MPGrowth": 2, "SpdGrowth": 0.45, "AtkGrowth": 9, "DefGrowth": 9, "MgkGrowth": 8, "ResGrowth": 11}
moogleJobs[7] = {"Name": "time mage", "BaseHP": 78, "BaseMP": 38, "BaseSpd": 57, "BaseAtk": 59, "BaseDef": 61, "BaseMgk": 89, "BaseRes": 96, "HPGrowth": 5, "MPGrowth": 6, "SpdGrowth": 0.50, "AtkGrowth": 5, "DefGrowth": 6, "MgkGrowth": 10, "ResGrowth": 10}
moogleJobs[8] = {"Name": "chocobo rider", "BaseHP": 74, "BaseMP": 9, "BaseSpd": 65, "BaseAtk": 65, "BaseDef": 72, "BaseMgk": 69, "BaseRes": 69, "HPGrowth": 5, "MPGrowth": 1, "SpdGrowth": 0.99, "AtkGrowth": 6, "DefGrowth": 7, "MgkGrowth": 6, "ResGrowth": 7}
moogleJobs[9] = {"Name": "flintlock", "BaseHP": 76, "BaseMP": 33, "BaseSpd": 58, "BaseAtk": 84, "BaseDef": 72, "BaseMgk": 78, "BaseRes": 76, "HPGrowth": 5, "MPGrowth": 5, "SpdGrowth": 0.52, "AtkGrowth": 8, "DefGrowth": 7, "MgkGrowth": 7, "ResGrowth": 7}
moogleJobs[10] = {"Name": "bard", "BaseHP": 74, "BaseMP": 31, "BaseSpd": 56, "BaseAtk": 70, "BaseDef": 58, "BaseMgk": 89, "BaseRes": 77, "HPGrowth": 6, "MPGrowth": 5, "SpdGrowth": 0.48, "AtkGrowth": 6, "DefGrowth": 6, "MgkGrowth": 9, "ResGrowth": 8}

seeqJobs = [dict for i in range(4)]
seeqJobs[0] = {"Name": "berzerker", "BaseHP": 94, "BaseMP": 4, "BaseSpd": 56, "BaseAtk": 91, "BaseDef": 69, "BaseMgk": 61, "BaseRes": 59, "HPGrowth": 7, "MPGrowth": 1, "SpdGrowth": 0.48, "AtkGrowth": 11, "DefGrowth": 6, "MgkGrowth": 6, "ResGrowth": 6}
seeqJobs[1] = {"Name": "ranger", "BaseHP": 86, "BaseMP": 10, "BaseSpd": 63, "BaseAtk": 78, "BaseDef": 82, "BaseMgk": 72, "BaseRes": 86, "HPGrowth": 7, "MPGrowth": 1, "SpdGrowth": 0.68, "AtkGrowth": 8, "DefGrowth": 8, "MgkGrowth": 7, "ResGrowth": 9}
seeqJobs[2] = {"Name": "lanista", "BaseHP": 88, "BaseMP": 19, "BaseSpd": 57, "BaseAtk": 86, "BaseDef": 84, "BaseMgk": 74, "BaseRes": 64, "HPGrowth": 7, "MPGrowth": 2, "SpdGrowth": 0.50, "AtkGrowth": 9, "DefGrowth": 9, "MgkGrowth": 7, "ResGrowth": 6}
seeqJobs[3] = {"Name": "viking", "BaseHP": 90, "BaseMP": 22, "BaseSpd": 59, "BaseAtk": 82, "BaseDef": 73, "BaseMgk": 78, "BaseRes": 97, "HPGrowth": 7, "MPGrowth": 3, "SpdGrowth": 0.54, "AtkGrowth": 8, "DefGrowth": 7, "MgkGrowth": 7, "ResGrowth": 11}

griaJobs = [dict for i in range(4)]
griaJobs[0] = {"Name": "hunter", "BaseHP": 84, "BaseMP": 23, "BaseSpd": 61, "BaseAtk": 84, "BaseDef": 66, "BaseMgk": 68, "BaseRes": 84, "HPGrowth": 6, "MPGrowth": 3, "SpdGrowth": 0.65, "AtkGrowth": 8, "DefGrowth": 6, "MgkGrowth": 7, "ResGrowth": 8}
griaJobs[1] = {"Name": "raptor", "BaseHP": 90, "BaseMP": 26, "BaseSpd": 60, "BaseAtk": 88, "BaseDef": 68, "BaseMgk": 82, "BaseRes": 68, "HPGrowth": 7, "MPGrowth": 3, "SpdGrowth": 0.63, "AtkGrowth": 9, "DefGrowth": 6, "MgkGrowth": 8, "ResGrowth": 6}
griaJobs[2] = {"Name": "ravager", "BaseHP": 94, "BaseMP": 18, "BaseSpd": 58, "BaseAtk": 92, "BaseDef": 88, "BaseMgk": 62, "BaseRes": 62, "HPGrowth": 7, "MPGrowth": 2, "SpdGrowth": 0.50, "AtkGrowth": 10, "DefGrowth": 9, "MgkGrowth": 6, "ResGrowth": 6}
griaJobs[3] = {"Name": "geomancer", "BaseHP": 82, "BaseMP": 36, "BaseSpd": 59, "BaseAtk": 79, "BaseDef": 90, "BaseMgk": 76, "BaseRes": 90, "HPGrowth": 6, "MPGrowth": 5, "SpdGrowth": 0.52, "AtkGrowth": 7, "DefGrowth": 11, "MgkGrowth": 7, "ResGrowth": 11}

allJobs = [humeJobs, vieraJobs, bangaaJobs, nuMouJobs, moogleJobs, seeqJobs, griaJobs]


###########################################################
# FUNCTION(S)


def get_job(): # Asks to input a job and returns the corresponding dictionary

    jobInput = input("\n\nEnter the character’s job: ").lower()

    while True:

        if "black mage" in jobInput:
            while True:
                if "hume" in jobInput:
                    return humeJobs[3]
                elif "moogle" in jobInput:
                    return moogleJobs[2]
                elif "nu mou" in jobInput:
                    return nuMouJobs[1]
                jobInput = input("\n\nHume, Nu Mou or Moogle?\n").lower()

        if "white mage" in jobInput:
            while True:
                if "hume" in jobInput:
                    return humeJobs[2]
                elif "viera" in jobInput:
                    return vieraJobs[1]
                elif "nu mou" in j:
                    return nuMouJobs[0]
                jobInput = input("\n\nHume, Nu Mou or Viera?\n").lower()

        if "time mage" in jobInput:
            while True:
                if "nu mou" in jobInput:
                    return nuMouJobs[3]
                elif "moogle" in jobInput:
                    return moogleJobs[7]
                jobInput = input("\n\nNu Mou or Moogle?\n").lower()

        if "hunter" in jobInput:
            while True:
                if "hume" in jobInput:
                    return humeJobs[11]
                elif "gria" in jobInput:
                    return griaJobs[0]
                jobInput = input("\n\nHume or Gria?\n").lower()

        if "thief" in jobInput:
            while True:
                if "hume" in jobInput:
                    return humeJobs[1]
                elif "moogle" in jobInput:
                    return moogleJobs[1]
                jobInput = input("\n\nHume or Moogle?\n").lower()

        if "illusionist" in jobInput:
            while True:
                if "hume" in jobInput:
                    return humeJobs[9]
                elif "nu mou" in jobInput:
                    return nuMouJobs[4]
                jobInput = input("\n\nHume or Nu Mou?\n").lower()

        if "archer" in jobInput:
            while True:
                if "hume" in jobInput:
                    return humeJobs[4]
                elif "viera" in jobInput:
                    return vieraJobs[3]
                jobInput = input("\n\nHume or Viera?\n").lower()


        for race in allJobs:
            for job in race: # We’re going to go trough jobs we’ve already checked
                if job["Name"] == jobInput:
                    return job

        jobInput = input("\n\nPlease enter a valid job: ").lower()



###########################################################
# MAIN


system(clear)

print("Hume jobs:", end="")
for job in humeJobs:
    print(" " + job["Name"], end="")
print(".")

print("Viera jobs:", end="")
for job in vieraJobs:
    print(" " + job["Name"], end="")
print(".")

print("Bangaa jobs:", end="")
for job in bangaaJobs:
    print(" " + job["Name"], end="")
print(".")

print("Nu Mou jobs:", end="")
for job in nuMouJobs:
    print(" " + job["Name"], end="")
print(".")

print("Moogle jobs:", end="")
for job in moogleJobs:
    print(" " + job["Name"], end="")
print(".")

print("Seeq jobs:", end="")
for job in seeqJobs:
    print(" " + job["Name"], end="")
print(".")

print("Gria jobs:", end="")
for job in griaJobs:
    print(" " + job["Name"], end="")
print(".")

job = get_job()
level = int(input("\nEnter the character’s level: "))
hp = job["HPGrowth"] * level + job["BaseHP"]
hp = job["HPGrowth"] * level + job["BaseHP"]
mp = job["MPGrowth"] * level + job["BaseMP"]
spd = job["SpdGrowth"] * float(level) + job["BaseSpd"]
atk = (job["AtkGrowth"] * level + job["BaseAtk"]) / 4
defense = (job["DefGrowth"] * level + job["BaseDef"]) /4
mgk = (job["MgkGrowth"] * level + job["BaseDef"]) /4
res = (job["ResGrowth"] * level + job["BaseRes"]) /4

system(clear)
print("HP:  " + str(hp))
print("MP:  " + str(mp))
print("Spd: " + str(spd))
print("Atk: " + str (atk))
print("Def: " + str (defense))
print("Mgk: " + str(mgk))
print("Res: " + str(res))

input()