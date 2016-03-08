#
# ---------------------------------FUNCTION TO CALCULATE THE PERCENTAGE VALUE-------------------------------------------------
def percentage(totalValue, percentageValue):
    """Function that receives two values. It's used to
    calculate percentage value"""

    print "The percentage value is: " + str((percentageValue  * 100) / totalValue)

#---------------------FIND WHICH CITIES HAVE AT LEAST TWO PARK AND RIDES WITHIN THEIR BOUNDARIES-------------------------------
from arcpy import env, Delete_management, GetCount_management, MakeFeatureLayer_management, SelectLayerByLocation_management
from arcpy.da import UpdateCursor

# Setting workspace
env.workspace = "C:\\learnPython\\data\\Lesson3PracticeExerciseB\\Washington.gdb"

# Name geography data of city
cityBoundaries = "CityBoundaries"

# Name of fields 
nameField = "NAME"
parkAndRideField = "HasTwoParkAndRides"

# Name of geography data of park and ride
parkAndRide = "ParkAndRide"

# Variables to count the total of city and the total of city with two or more park and ride 
CityWithTwoParkAndRides = 0
totalCity = 0

# Try find which cities have at least two park and rides within their boundaries
try:
    
    #
    with UpdateCursor(cityBoundaries, (nameField, parkAndRideField)) as cityRows:

        # For each feature of city in cityBoundaries geography data
        for row in cityRows:

            # Get the name of each city
            nameCity = row[0]

            # 
            queryString = '"' + nameField + '" = ' + "'" + nameCity + "'"

            # Make a feature layer of just the current city polygon
            # The queryString is reponsible for select only the feature of city
            MakeFeatureLayer_management(cityBoundaries, "CurrentCityLayer", queryString) 
            MakeFeatureLayer_management(parkAndRide, "ParkAndRide_lry")

            # Selecty by location all feature of park and ride that contain in current city
            SelectLayerByLocation_management("ParkAndRide_lry", "CONTAINED_BY", "CurrentCityLayer")

            # Get the total value of park and ride for each city
            countPark = GetCount_management("ParkAndRide_lry")
            totalPark = int(countPark.getOutput(0))

            # Count of city in cityBoundaries
            totalCity += 1

            # If the total park and rise is bigger then 1
            if totalPark > 1:

                # The row in field HasTwoParkAndRides update to "True"
                row[1] = "True"
            
                # Count each city has than more that two park and ride in your limits
                CityWithTwoParkAndRides += 1

            else:
            
                # Go to the next feature
                pass

            # Delete the courrent layers
            Delete_management("CurrentCityLayer")
            Delete_management("ParkAndRide_lry")
            
# If happen some error
except:

    # Show the message
    print "It was not possible find which cities have at least two park and rides within their boundaries"
        
# ---------------------------------SHOW PERCENTAGE VALUE---------------------------------------

# Show the percentage value
percentage(totalCity, CityWithTwoParkAndRides)
