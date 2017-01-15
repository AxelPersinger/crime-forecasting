########################################################################################################################
#                                                  IMPORT LIBRARIES
#
#   getCoords - get coordinates from file
########################################################################################################################
import getCoords


########################################################################################################################
#                                                  GLOBAL VARIABLES
#
#   portland - portland map into the area we want (Portland, OR)
########################################################################################################################
coords = getCoords.getSet("A")
print coords

########################################################################################################################
#                                                  FUNCTION: getMedianDistance
#   Gets the median distance for x and y returns a tuple (medianX, medianY)
########################################################################################################################
def getMedianDistance(coords):
    return 0

########################################################################################################################
#                                                  FUNCTION: distance
#   Returns distance between x1 and x2
########################################################################################################################
def distance(a, b):
    return sqrt(float(a**2) - float(b**2))