#
#---------------SELECTS ALL THE PARK AND RIDE FACILITIES IN A GIVEN CITY AND SAVES THEN OUT A NEW FEATURE CLASS-----------------
from arcpy import env, Delete_management, CopyFeatures_management, MakeFeatureLayer_management, SelectLayerByLocation_management

# Setting workspace
env.workspace = "C:\\learnPython\\data\\Lesson3PracticeExerciseD\\Washington.gdb"

# Name of feature park and rides
parkAndRide = "ParkAndRide"

# Name of featue city boundaries 
cityBoundaries = "CityBoundaries"

# Name of field with the name of cities
nameField = 'NAME'

# Name of city for select layer by location
nameCity = 'Federal Way'

# Try selects all the park and ride facilities in a given city and saves them out to a new feature class
try:

    # SQL to select only one city
    queryString = '"' + nameField + '" = ' + "'" + nameCity + "'" # It means the same that: " nameField + " = ' nameCity '
    
    # Name of new layer of city
    nameCityLayer = nameCity.replace(" ","_") + '_lyr'

    # Make a feature layers
    MakeFeatureLayer_management(parkAndRide,"parkAndRide_lry")      
    MakeFeatureLayer_management(cityBoundaries, nameCityLayer, queryString)

    # Select all park and ride into of only city
    SelectLayerByLocation_management("parkAndRide_lry", "CONTAINED_BY", nameCityLayer)

    # Name of new feature class
    nameFeatureOut = nameCity + '_ParkAndRide'

    # Create a new feature class only with park and ride into of city
    CopyFeatures_management("parkAndRide_lry", nameOut)

    # Detele feature layers
    Delete_management("parkAndRide_lry")
    Delete_management(nameCityLayer)

# If happen some error
except:

    # Show the message
    print 'It was not possible selects all the park and ride facilities in a given city and saves them out to a new feature class'
