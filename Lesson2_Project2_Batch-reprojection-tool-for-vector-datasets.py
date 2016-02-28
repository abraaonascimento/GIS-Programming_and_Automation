# FIRST TESTE

from arcpy import env,  Describe, ListFeatureClasses

standard_folder = "C:\\learnPython\\data\\lesson2_2"
standard_file = "C:\\learnPython\\data\\lesson2_2\\StateRoutes.shp"

# Get a list of all feature classes in the standard folder
env.workspace = standar_folder
featureClass = ListFeatureClasses()


# Get spatial reference of standar file
desc_st = Describe(standard_file)
sr_st = desc.spatialReference

try: 
# Loop through all feature classes in standar folder
    for feature in featureClass:

        # Describe the spatial reference of feature
        desc = Describe(feature)
        sr = desc.spatialReference

        # If the name of spatial reference for equal
        # the standard  spatial reference show message
        # about this and pass to next feature
        if sr.name == sr_st.name:
            print "This file already have the Standard spacial reference"
            pass

        else:
            # change spacial reference
            # print message to change
            # save new spacial file in standard folder with name of file + reproject
                # name = str(shp)[:-4]
                # name reproject = "_reproject"
                # CreateFeatureclass_management
            # print save new spacial file

# If happen some error 
except:
    # Show messages for error
    print GetMessages()
