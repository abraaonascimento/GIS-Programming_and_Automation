#------------MAKES A SEPARATE SHAPEFILE FOR EACH OF THESE TYPES OF AMENITIES (SCHOOLS, HOSPITALS, PLACES OF WORSHIP) WITHIN THE BOUNDARY OF EL SALVADOR------------
from arcpy import env, AddField_management, CopyFeatures_management,  Delete_management, MakeFeatureLayer_management, SelectLayerByLocation_management, UpdateCursor
from arcpy.da import UpdateCursor

# Setting the workspace
env.workspace = "C:\\learnPython\\data\\Project3"

# Input the names of geographic data
centralAmericaBoundaries = "CentralAmerica.shp"
osmPoints = "OSMpoints.shp"

# The name field of geographic data of points by Open Street Map
nameFieldAmenity = "Amenity"
nameFieldCountry = "NAME"

# Input the names of amenities and the name of country
amenities = ["school","hospital","place_of_worship"]
country = "El Salvador"

try:
    #
    queryStringCountry = '"' + nameFieldCountry + '" = ' + "'"  + country + "'"
    nameCountryLayer = country + "lyr"
    MakeFeatureLayer_management(centralAmericaBoundaries, nameCountryLayer, queryStringCountry)

    for typeAmenities in amenities:

        # SQL pick up the type amenities
        queryStringAmenities = '"' + nameFieldAmenity + '" = ' + "'"  + typeAmenities + "'"

        # The name of new feature layer 
        nameAmenitiesLayer = typeAmenities + "lyr"

        # Mame a feature layer of type amenities 
        MakeFeatureLayer_management(osmPoints, nameAmenitiesLayer, queryStringAmenities)

        # Select only amanities into the country El Salvador
        SelectLayerByLocation_management(nameAmenitiesLayer, "CONTAINED_BY", nameCountryLayer)

        # Makes a separate shapefile for each types of amenities 
        CopyFeatures_management(nameAmenitiesLayer, typeAmenities)

        # Get the new separete shapefile
        amenitiesTable = typeAmenities + '.dbf'
        
        #
        newField = "source"

        # Add new field called 'source'
        AddField_management(amenitiesTable, newField, "TEXT", 100)
        
        with UpdateCursor(typeAmenities + ".shp", newField) as amenitiesRows:

            for row in amenitiesRows:

                row[0] = "OpenStreetMap"

                amenitiesRows.updateRow(row)
except:
    print 'It was not possible makes a separete shapefile for amenities'
