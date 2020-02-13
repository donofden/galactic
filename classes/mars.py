class Mars:
    
    Name = "Mars"

    def __init__(self):
        """
        Our constructor class that instantiates Mars.
        """
        self.planet = self.Name

    def calculateWeight(self, weightOnEarth):
        weightInMars = ((weightOnEarth / 9.81)* 3.711)
        return weightInMars
