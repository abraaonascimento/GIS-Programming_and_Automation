# TESTE 1
# ----------------------- FUNCTION TO CALCULATE THE PERCENTAGE VALUE-----------------------------------

def percentage(totalValue, percentageValue):
    """Function that receives two values. It's used to
    calculate percentage value"""

    print "The percentage value is: " + str((percentageValue  * 100) / totalValue)

#-------------------------
from arcpy import env, GetCount_management, MakeFeatureLayer_management, SelectLayerByLocation_management
from arcpy.da import UpdateCursor

# Setting workspace
env.workspace = "C:\\learnPython\\data\\Lesson3PracticeExerciseA\\Washington.gdb"

# Name and field of city geography data
cities = "CityBoundaries"
nameField = "NAME"
parkAndRideField = "HasTwoParkAndRides"   # Name of column for storing the Park & Ride information
cityIDStringField = "CI_FIPS"

# Name of park/ride geography data
parkAndRide = "ParkAndRide"

#arcpy.MakeFeatureLayer_management(parkAndRide, "ParkAndRideLayer")
#with arcpy.da.UpdateCursor(cityBoundaries, (cityIDStringField, parkAndRideField)) as cityRows:
    #for city in cityRows:
        # Create a query string for the current city    
        #cityIDString = city[0]
        #queryString = '"' + cityIDStringField + '" = ' + "'" + cityIDString + "'"
        # Make a feature layer of just the current city polygon    
        #arcpy.MakeFeatureLayer_management(cityBoundaries, "CurrentCityLayer", queryString)
        
with UpdateCursor(cities, (nameField,)) as cursor: #selecionar o nome

        for city in cursor:

            queryString = '"' + cityIDStringField + '" = ' + "'" + cityIDString + "'"

            MakeFeatureLayer_management(parkAndRide, "ParkAndRide_lry")
            MakeFeatureLayer_management(city, "city_lry")

            SelectLayerByLocation_management("city_lry", "CONTAINED_BY", "ParkAndRide_lry")

            countPark = GetCount_management("ParkAndRide_lry")
            totalPark = int(city.getOutput(0))

            if totalPark > 1:
                
                # Update row to 'True'
                row[0] = "True"

                
            else:
                pass
