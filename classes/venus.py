
class Venus:

    Name = "Venus"

    def __init__(self):
        """
        Our constructor class that instantiates venus.
        """
        self.planet = self.Name

    def calculateWeight(self, weightOnEarth):
        weightInVenus = ((weightOnEarth / 9.81)* 8.87)
        return weightInVenus