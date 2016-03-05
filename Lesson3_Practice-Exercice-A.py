# Version1
#-------------------------------------
from arcpy import env, ListFeatureClasses, MakeFeatureLayer_management, SelectLayerByLocation_management
import arcpy

#
env.workspace = "C:\\learnPython\\data\\Lesson3PracticeExerciseA\\Washington.gdb"

#
cities = "CityBoundaries"
nameField = "HasParkAndRide"

#
parkAndRide = "ParkAndRide"


try:

    #
    MakeFeatureLayer_management(cities,"CityBoundaries_lyr")
    MakeFeatureLayer_management(parkAndRide,"ParkAndRide_lry")


    # Select only the cities that contain point of park or ride
    SelectLayerByLocation_management("CityBoundaries_lyr", "CONTAINS", "ParkAndRide_lry")

except:
    print 'error'

#
try:
    
    with arcpy.da.UpdateCursor("CityBoundaries_lyr", (nameField,)) as cursor:

        #
        for row in cursor:

            # 
            row[0] = "True"
except:
#    print "error!"

#
city = arcpy.GetCount_management("CityBoundaries")
totalCity = int(city.getOutput(0))

citySelected = arcpy.GetCount_management("CityBoundaries_lyr")
totalCitySelected = int(citySelected.getOutput(0))

def percentage(totalValue, percentageValue):
    """ The function recives two values. It's used to
    calculate percentage value"""

    print "The percentage value is: " (percentageValue  * 100) / totalValue


def main():

    # 
    percentage(totalCity, totalCitySelected)

if __name__ == "__main__":
    main()
