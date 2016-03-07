# FIRST TESTE
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

        nameCity = city[0]
        # Create a query string for the current city    
        #cityIDString = city[0]
        queryString = '"' + nameField + '" = ' + "'" + nameCity + "'"
        # Make a feature layer of just the current city polygon    
        MakeFeatureLayer_management(cityBoundaries, "CurrentCityLayer", queryString)
        MakeFeatureLayer_management(parkAndRide, "ParkAndRide_lry")

        SelectLayerByLocation_management("ParkAndRide_lry", "CONTAINED_BY", "CurrentCityLayer")

        # Get the total value of cities in CityBoundaries 
        city = GetCount_management("CurrentCityLayer")
        totalCity = int(city.getOutput(0))

        Park = GetCount_management("ParkAndRide_lry")
        totalPark = int(city.getOutput(0))

        print queryString
        print totalCity

        print totalPark

        Delete_management("CurrentCityLayer")
        Delete_management("CurrentCityLayer")

        break
