class Jupiter:
    
    Name = "Jupiter"

    def __init__(self):
        """
        Our constructor class that instantiates Jupiter.
        """
        self.planet = self.Name

    def calculateWeight(self, weightOnEarth):
        weightInJupiter = ((weightOnEarth / 9.81)* 24.79)
        return weightInJupiter
