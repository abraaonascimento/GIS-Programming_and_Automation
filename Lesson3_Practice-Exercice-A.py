#
# ----------------------- FUNCTION TO CALCULATE THE PERCENTAGE VALUE-----------------------------------

def percentage(totalValue, percentageValue):
    """Function that receives two values. It's used to
    calculate percentage value"""

    print "The percentage value is: " + str((percentageValue  * 100) / totalValue)

#---------- SELECT FEATURES BY LOCATION AND UPDATE A FIELD FOR THE SELECTED FEATURES -------------------
from arcpy import env, GetCount_management, MakeFeatureLayer_management, SelectLayerByLocation_management
from arcpy.da import UpdateCursor

# Setting workspace
env.workspace = "C:\\learnPython\\data\\Lesson3PracticeExerciseA\\Washington.gdb"

# Name and field of city geography data
cities = "CityBoundaries"
nameField = "HasParkAndRide"

# Name of park/ride geography data
parkAndRide = "ParkAndRide"

# Try make layers
try:
    # Make a city layer and park/ride layer
    MakeFeatureLayer_management(cities,"CityBoundaries_lyr")
    MakeFeatureLayer_management(parkAndRide,"ParkAndRide_lry")

    # Select only the cities that contain point of park and ride
    SelectLayerByLocation_management("CityBoundaries_lyr", "CONTAINS", "ParkAndRide_lry")

# If happen some error
except:

    # show the massage
    print 'It not possible to make a layer'

# Try update field
try:

    # Select the field HasParkAndRide of CityBoundaries layer 
    with UpdateCursor("CityBoundaries_lyr", (nameField,)) as cursor:

        # For each row in field
        for row in cursor:

            # Update row to 'True'
            row[0] = "True"

# If happen some error            
except:
    # Show the massage
    print "It not possible update a field: ", nameField, "for the selected features"

# Get the total value of cities in CityBoundaries 
city = GetCount_management("CityBoundaries")
totalCity = int(city.getOutput(0))

# Get the total value of cities seleted in CityBoundaries layer
citySelected = GetCount_management("CityBoundaries_lyr")
totalCitySelected = int(citySelected.getOutput(0))

# ---------------------------------SHOW PERCENTAGE VALUE---------------------------------------

# Show the percentage value
percentage(totalCity, totalCitySelected)
