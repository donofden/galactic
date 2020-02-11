
class Uranus:

    Name = "Uranus"

    def __init__(self):
        """
        Our constructor class that instantiates uranus.
        """
        self.planet = self.Name

    def calculateWeight(self, weightOnEarth):
        weightInUranus = ((weightOnEarth / 9.81)* 8.69)
        return weightInUranus