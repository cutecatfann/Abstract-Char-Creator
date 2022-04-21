from abc import ABC, abstractmethod

class SpeciesInt(ABC):
    """
    Abstract class for all species. Subclasses can easily inherent from here from the abstract method.
    Currently, 6 abstract methods are included in the class for sub classes to build from.
    """
    @abstractmethod
    def getModifiers(self) -> dict:
        """ Gets the species base bonus modifiers to stats.
            Returns list of modifed stats."""
        pass

    @abstractmethod 
    def speciesMagic(self) -> int:
        """ Gets the species base magic amount.
            Returns int for level of magic in species."""
        pass

    @abstractmethod  
    def getHeight(self, heightRange: dict) -> int:
        """ Gets the species height range.
            Randomly selects a number within the range.
            Returns int for height."""
        pass

    @abstractmethod 
    def getSize(self, sizeRange: dict) -> int:
        """ Gets the species size range.
            Randomly selects a number within the range.
            Returns int for size."""
        pass
    
    @abstractmethod
    def returnAnimosity(self, otherSpecies: dict) -> dict:
        """ Gets how other species' level of animosity to certain species
            Returns dict with all values relavent to certain species listed."""
        pass

    @abstractmethod 
    def clanName(self, allClanNames: dict) -> str:
        """ Gets dict with all clan names for all species.
            Returns string with selected clan name."""
        pass
