class Neptune:
    
    Name = "Neptune"

    def __init__(self):
        """
        Our constructor class that instantiates neptune.
        """
        self.planet = self.Name

    def calculateWeight(self, weightOnEarth):
        weightInNeptune = ((weightOnEarth / 9.81)* 11.15)
        return weightInNeptune
