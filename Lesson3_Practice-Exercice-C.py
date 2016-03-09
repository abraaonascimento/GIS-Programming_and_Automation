#----SELECT ALL PARK AND RIDE FACILITIES WITH A CAPACITY OF MORE THAN 500  
#                                   PARKING SPACES AND PUT THEN INTO THEIR OWN FEATURE CLASS--
from arcpy import env, Delete_management, MakeFeatureLayer_management, CopyFeatures_management

# Setting workspace
env.workspace = "C:\\learnPython\\data\\Lesson3PracticeExerciseC\\Washington.gdb"

# Name of geography data of park and rides
parkAndRide = "ParkAndRide"

# Name of field
ApproxParFiled = "Approx_Par"

# query SQL for select only the park and ride with more that 500 parking spaces
queryString = '"Approx_Par" > 500'

# Try Select all park and ride facilities with a capacity of more than 500 parking spaces and
# put them into their own feature class
try:

    # Create a new shapefile with park and rides that have more than 500 parking spaces
    MakeFeatureLayer_management(parkAndRide, "parkAndRide_500_lyr", queryString)
    CopyFeatures_management("parkAndRide_500_lyr", "parkAndRide500")

    # Close all the features
    Delete_management("parkAndRide_500_lyr")

    print 'Success!'

# If happen some error 
except:

    # Show the message
    print "It was not possible to do this process."
