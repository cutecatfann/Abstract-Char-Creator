from abc import ABC, abstractmethod

class Job(ABC):
    """
    Creates a job with all relavent parts. There are seven abstract methods currently contained.
    It is an abstract class, which allows other classes to build on top of it.
    """
    @abstractmethod
    def getSkillsModifier(self, baseStats: dict) -> dict:
        """ Gets list of job base stat modifiers. 
            Returns a dict of the modified base stats.
        """
        pass

    @abstractmethod
    def combatMod(self) -> dict:
        """ Gets the combat modifer. 
            Returns a dict of the modified base stats.
        """
        pass

    @abstractmethod
    def levelBonus(self) -> int:
        """Returns the level bonus for job.
        """
        pass

    @abstractmethod
    def skills(self) -> list:
        """ Returns list of base job skills.
        """
        pass

    @abstractmethod
    def weapon(self) -> str:
        """ Returns job's base weapon.
        """
        pass

    @abstractmethod
    def magicBonus(self) -> int:
        """ Returns the job magic modifier.
        """
        pass

    @abstractmethod
    def jobWeakness(self) -> list:
        """ Returns base weaknesses associated with job class.
        """
        pass
