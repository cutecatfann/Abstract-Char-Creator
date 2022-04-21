from jobInterface import Job

class Healer(Job):
    """
    Creates the Healer job. Includes the data for the characteristics for base job.
    It inherents from the abstract method for Jobs.
    """

    def getSkillsModifier(self, baseStats: dict) -> dict:
        skillMods = {}
        return skillMods

    def combatMod(self) -> dict:
        combat = {}
        return combat

    def levelBonus(self) -> int:
        bonus = 0
        return bonus

    def skills(self) -> list:
        skills = []
        return skills

    def weapon(self) -> str:
        weapon = ""
        return weapon

    def magicBonus(self) -> int:
        magicJobBonus = 0
        return magicJobBonus

    def jobWeakness(self) -> list:
        basicWeaknesses = []
        return basicWeaknesses
