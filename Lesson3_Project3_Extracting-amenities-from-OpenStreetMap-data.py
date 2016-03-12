# MAKES A SEPARATE SHAPEFILE FOR EACH OF THESE TYPES OF AMENITIES (SCHOOLS, HOSPITALS, PLACES OF WORSHIP) WITHIN THE BOUNDARY OF EL SALVADOR ----------------------------------
from arcpy import env, AddField_management, CopyFeatures_management,  MakeFeatureLayer_management, UpdateCursor
from arcpy.da import UpdateCursor

# Setting the workspace
env.workspace = "C:\\learnPython\\data\\Project3"

# Input the names of geographic data
centralAmericaBoundaries = "CentralAmerica.shp"
osmPoints = "OSMpoints.shp"

# Input the names of amenities and the name of country
amenities = ["school","hospital","place_of_worship"]
country = "El Salvador"

# The name field of geographic data of points by Open Street Map
nameFieldAmenity = "Amenity"

try:
    # For each type amenities in amenities list
    for typeAmenities in amenities:

        # SQL pick up the type amenities
        queryString = '"' + nameFieldAmenity + '" = ' + "'"  + typeAmenities + "'"

        # The name of new feature layer 
        nameAmenitiesLayer = typeAmenities + "lyr"
    
        # Mame a feature layer of type amenities 
        MakeFeatureLayer_management(osmPoints, nameAmenitiesLayer, queryString)

        # Makes a separate shapefile for each types of amenities 
        CopyFeatures_management(nameAmenitiesLayer, typeAmenities)

        # get the new separete shapefile
        amenitiesTable = typeAmenities + '.dbf'

        # Add new field called 'source'
        AddField_management(amenitiesTable, newField, "TEXT", 100)

        #
        newField = "source"
        
        with UpdateCursor(typeAmenities + ".shp", newField) as amenitiesRows:

            for row in amenitiesRows:

                row[0] = "OpenStreetMap"

                amenitiesRows.updateRow(row)
except:
    print 'It was not possible makes a separete shapefile for amenities'
