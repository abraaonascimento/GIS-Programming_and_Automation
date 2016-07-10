#---------------------- TASK 1 - MAKE A RANDOW POINT SHAPEFILE ------------------------------
from arcpy import CreateRandomPoints_management

# Setting the polygon shapefile 
geographicData = "C:\\data\\shapefile.shp"

# Setting the field name with value of people by census tract
fieldName = "N_PEOPLE"

# Setting the path out
geographicDataOut = "C:\\data\\out"

# Setting the name to new geographic data (randow shapefile)
nameNewGeographicData = "randowPeople"

try:
  
  # Create a randow shapefile
  arcpy.CreateRandomPoints_management(geographicDataOut, nameNewGeographicData, geographicData, "", fieldName)

except:
  print GetMessages()
