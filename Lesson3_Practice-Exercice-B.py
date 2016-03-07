# TESTE 1
# ----------------------- FUNCTION TO CALCULATE THE PERCENTAGE VALUE-----------------------------------

def percentage(totalValue, percentageValue):
    """Function that receives two values. It's used to
    calculate percentage value"""

    print "The percentage value is: " + str((percentageValue  * 100) / totalValue)

#----------------------------------------------
from arcpy import env, Delete_management, GetCount_management, MakeFeatureLayer_management, SelectLayerByLocation_management
from arcpy.da import UpdateCursor

# Setting workspace
env.workspace = "C:\\learnPython\\data\\Lesson3PracticeExerciseB\\Washington.gdb"

# Name and field of city geography data
cityBoundaries = "CityBoundaries"
nameField = "NAME"
parkAndRideField = "HasTwoParkAndRides"   # Name of column for storing the Park & Ride information

# Name of park/ride geography data
parkAndRide = "ParkAndRide"

with UpdateCursor(cityBoundaries, (nameField, parkAndRideField)) as cityRows:
    for city in cityRows:

        name = city[0]
        # Create a query string for the current city    
        #cityIDString = city[0]
        queryString = '"' + nameField + '" = ' + "'" + name + "'"
        # Make a feature layer of just the current city polygon    
        MakeFeatureLayer_management(cityBoundaries, "CurrentCityLayer", queryString)

        # Get the total value of cities in CityBoundaries 
        city = GetCount_management("CurrentCityLayer")
        totalCity = int(city.getOutput(0))

        print queryString
        print totalCity

        Delete_management("CurrentCityLayer")

        break
