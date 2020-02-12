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

print("Enter your Weight: ")
weight = int(input())

earthObj = Earth()
printOut(earthObj.planet, weight)

mercuryObj = Mercury()
calculatedWeight = mercuryObj.calculateWeight(weight)
printOut(mercuryObj.planet, calculatedWeight)

venusObj = Venus()
calculatedWeight = venusObj.calculateWeight(weight)
printOut(venusObj.planet, calculatedWeight)

marsObj = Mars()
calculatedWeight = marsObj.calculateWeight(weight)
printOut(marsObj.planet, calculatedWeight)

jupiterObj = Jupiter()
calculatedWeight = jupiterObj.calculateWeight(weight)
printOut(jupiterObj.planet, calculatedWeight)

saturnObj = Saturn()
calculatedWeight = saturnObj.calculateWeight(weight)
printOut(saturnObj.planet, calculatedWeight)

uranusObj = Uranus()
calculatedWeight = uranusObj.calculateWeight(weight)
printOut(uranusObj.planet, calculatedWeight)

neptuneObj = Neptune()
calculatedWeight = neptuneObj.calculateWeight(weight)
printOut(neptuneObj.planet, calculatedWeight)

plutoObj = Pluto()
calculatedWeight = plutoObj.calculateWeight(weight)
printOut(plutoObj.planet, calculatedWeight)

sunObj = Sun()
calculatedWeight = sunObj.calculateWeight(weight)
printOut(sunObj.planet, calculatedWeight)
