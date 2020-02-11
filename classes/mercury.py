class Mercury:
    
    Name = "Mercury"

    def __init__(self):
        """
        Our constructor class that instantiates mercury.
        """
        self.planet = self.Name

    def calculateWeight(self, weightOnEarth):
        weightInMerucry = ((weightOnEarth / 9.8)* 3.7)
        return weightInMerucry