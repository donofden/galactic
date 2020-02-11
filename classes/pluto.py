class Pluto:
    
    Name = "Pluto"

    def __init__(self):
        """
        Our constructor class that instantiates pluto.
        """
        self.planet = self.Name

    def calculateWeight(self, weightOnEarth):
        weightInPluto = ((weightOnEarth / 9.81)* 0.65)
        return weightInPluto