class Saturn:
    
    Name = "Saturn"

    def __init__(self):
        """
        Our constructor class that instantiates saturn.
        """
        self.planet = self.Name

    def calculateWeight(self, weightOnEarth):
        weightInSaturn = ((weightOnEarth / 9.81)* 10.44)
        return weightInSaturn
