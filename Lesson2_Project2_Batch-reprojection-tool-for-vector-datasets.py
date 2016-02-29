import time
from time import gmtime, strftime

from arcpy import env,  Describe, GetMessages, GetParameterAsText, ListFeatureClasses, Project_management, SpatialReference

# Start scrpit
start_time = time.time()

# Get the parameters of project2 tool
input_folder = GetParameterAsText(0)
input_file = GetParameterAsText(1)

# input_folder = "C:\\learnPython\\data\\lesson2_2"
# input_file = "C:\\learnPython\\data\\lesson2_2\\StateRoutes.shp"

print("Executing: Project2 tool " + str(input_folder) + " " + str(input_file))
print ("Start Time: " + strftime("%a, %d %b %Y %H:%M:%S 2016", gmtime()))
print ("Running a script Project2-Batch-reprojection-tool-for-vector-datasets")
# Get a list of all feature classes in the standard folder
env.workspace = input_folder
featureClass = ListFeatureClasses()

# Get spatial reference of standard file
desc_standard_file = Describe(input_file)
sr_standard_file = desc_standard_file.SpatialReference

# list for keep the reproject files names
l = []
try: 

    #Loop through all feature classes in standar folder
    for feature in featureClass:

        # Describe the spatial reference of feature
        desc = Describe(feature)
        sr = desc.SpatialReference

        # If the name of spatial reference is equal to
        # the standard  spatial reference, show message
        # about this and pass to next feature
        if sr.name == sr_standard_file.name:
            print ("This file: " + str(feature) + ", already have the standard spatial reference")
            pass

        # If the name of spatial reference is different to
        # the standard  spatial reference
        # reproject file
        else:

            # Get spatial reference
            coor_system = str(sr_standard_file.name)
            coor_system =  coor_system.replace("_", " ") + " (US Feet)"
            coor_system = SpatialReference(coor_system)
        
            # Output name
            feature_name = feature[:-4]
            out_name = "\\" + feature_name + "_projected"

            # reproject file
            Project_management(feature, input_folder + out_name, coor_system)

            print ("Projected: " + str(feature))
# If happen some error 
except:
    # Show messages for error
    print GetMessages()

print "Completed script Project2"
end_time = time.time()
print ("End Time: " + strftime("%a, %d %b %Y %H:%M:%S 2016", gmtime()) + ", Elaped Time: " + str(end_time - start_time)[:-5] + " seconds")
