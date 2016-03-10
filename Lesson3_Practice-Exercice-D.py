#-- TESTE1
from arcpy import env, Delete_management, MakeFeatureLayer_management, CopyFeatures_management, SelectLayerByLocation_management

# Setting workspace
env.workspace = "C:\\learnPython\\data\\Lesson3PracticeExerciseD\\Washington.gdb"

# Name of geography data of park and rides
parkAndRide = "ParkAndRide"

cityBoundaries = "CityBoundaries"
nameField = 'NAME'

nameCity = 'Federal Way'

nameCityLayer = nameCity + '_lyr'

nameOut = nameCity + '_ParkAndRide'

queryString = '"' + nameField + '" = ' + "'" + nameCity + "'" # It means that: " nameField + " = ' nameCity '

MakeFeatureLayer_management(parkAndRide,"ParkAndRide_lry")
        
MakeFeatureLayer_management(cityBoundaries, nameCityLayer, queryString)

SelectLayerByLocation_management("ParkAndRide_lry", "CONTAINED_BY", nameCityLayer)

CopyFeatures_management("parkAndRide_500_lyr", nameOut)

Delete_management("ParkAndRide_lry")
Delete_management(nameCityLayer)
