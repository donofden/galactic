class Sun:

    Name = "Sun"

    def __init__(self):
        """
        Our constructor class that instantiates sun.
        """
        self.planet = self.Name

    def calculateWeight(self, weightOnEarth):
        weightInSun = ((weightOnEarth / 9.81)* 274)
        return weightInSun