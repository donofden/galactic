from classes.earth import Earth
from classes.mercury import Mercury
from classes.venus import Venus
from classes.mars import Mars
from classes.jupiter import Jupiter
from classes.saturn import Saturn
from classes.uranus import Uranus
from classes.neptune import Neptune
from classes.pluto import Pluto
from classes.sun import Sun

def printOut(planet, weight):
    """
    To beautify the output.
    """
    roundValue = str(round(weight, 2))
    planetLen = len(planet)
    spaceFiller = " " * (8 - planetLen)
    print(planet + spaceFiller + " : " + roundValue," ")

class WeightCalculator:

    def get_weight(self):
        """
        To get input from user.
        """
        self.weight = int(input('Enter your Weight:'))

    def run(self):
        """
        Calculate the weight in other planets
        """
        self.get_weight()
        earthObj = Earth()
        printOut(earthObj.planet, self.weight)

        mercuryObj = Mercury()
        calculatedWeight = mercuryObj.calculateWeight(self.weight)
        printOut(mercuryObj.planet, calculatedWeight)

        venusObj = Venus()
        calculatedWeight = venusObj.calculateWeight(self.weight)
        printOut(venusObj.planet, calculatedWeight)

        marsObj = Mars()
        calculatedWeight = marsObj.calculateWeight(self.weight)
        printOut(marsObj.planet, calculatedWeight)

        jupiterObj = Jupiter()
        calculatedWeight = jupiterObj.calculateWeight(self.weight)
        printOut(jupiterObj.planet, calculatedWeight)

        saturnObj = Saturn()
        calculatedWeight = saturnObj.calculateWeight(self.weight)
        printOut(saturnObj.planet, calculatedWeight)

        uranusObj = Uranus()
        calculatedWeight = uranusObj.calculateWeight(self.weight)
        printOut(uranusObj.planet, calculatedWeight)

        neptuneObj = Neptune()
        calculatedWeight = neptuneObj.calculateWeight(self.weight)
        printOut(neptuneObj.planet, calculatedWeight)

        plutoObj = Pluto()
        calculatedWeight = plutoObj.calculateWeight(self.weight)
        printOut(plutoObj.planet, calculatedWeight)

        sunObj = Sun()
        calculatedWeight = sunObj.calculateWeight(self.weight)
        printOut(sunObj.planet, calculatedWeight)

if __name__ == '__main__':
    wc = WeightCalculator()
    wc.run()