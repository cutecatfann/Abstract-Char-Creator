from speciesInterface import SpeciesInt

class Dragon(SpeciesInt):
    """
    Creates the specific base Dragon species. It inherents from the abstract SpeciesInterface,
    and includes the data needed for the basic Dragon species.
    """

    def getModifiers(self) -> dict:
        statMods = {}
        return statMods

    def speciesMagic(self) -> int:
        magic = 0
        return magic

    def getHeight(self, heightRange: dict) -> int:
        height = 0
        return height

    def getSize(self, sizeRange: dict) -> int:
        size = 0
        return size

    def returnAnimosity(self, otherSpecies: dict) -> dict:
        animosity = {}
        return animosity

    def clanName(self, allClanNames: dict) -> str:
        clanName = ""
        return clanName
