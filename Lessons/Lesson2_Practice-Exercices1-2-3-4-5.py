#--------------------- Practice 1 - Find the spaces in a list of names -------------------------
print "Practice 1 - Find the spaces in a list of names"
print ""

# List of names
beatles = ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"]

# Show in each name of list the message "There is a space in _______'s name
# at character ____." with name and value
for name in beatles:
    print("There is a space in" + name + "'s name at character "+ str(name.index(" ")) + ".")

print "end practice 1 !"
print ""

#----------------- Practice 2 - Convert the names to a "Last, First" format -------------------
print 'Practice 2 - Convert the names to a "Last, First" format'
print ""

# List of names
beatles = ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"]

# Convert the names to a "Last, First" format
for name in beatles:
	space = name.index(" ")
	first_name = name[:space]
	last_name = name[space+1:]
	print (last_name + " " + first_name)

print "end practice 2"
print ""

# --------------------- Practice 3 - Convert scores to letter grades ---------------------------
# Score from 1-100 
score = range(1,101)

# Show letter grades like below,
"""
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: <60
"""
print("A: " + str(score[89]) + "-" + str(score[99]))
print("B: " + str(score[79]) + "-" + str(score[88]))
print("C: " + str(score[69]) + "-" + str(score[78]))
print("D: " + str(score[59]) + "-" + str(score[68]))
print("F: <" + str(score[59]))

print"end practice 3!"
print""

#-------------------- Practice 4 - Create copies of a template shapefile -----------------------
from arcpy import env, CreateFeatureclass_management, GetMessages

try:
    # My workspace
    env.workspace =  "C:\\learnPython\\data"

    # Template shapefile
    template = "Precip2008Readings.shp"

    # List with years: 2009, 2010, 2011 and 2012
    for year in range(2009,2013):

        # Name for new file
        newfile = "Precip" + str(year) + "Readings.shp"

        # Create four empty copies of file tamplate Precip2008Readings.shp
        CreateFeatureclass_management(env.workspace, newfile, "POINT", template,
                                            "DISABLED", "DISABLED", template)
# If happen some error
except:
    # Show messages for error
    print GetMessages()

# ------------------ Practice 5 - Clip all feature classes in a geodatabase ---------------------
from arcpy import env, AddMessage, Clip_analysis, ListFeatureClasses
 
# Create directors files
usa_workspace = "C:\\learnPython\\data\\USA.gdb"
iowa_data = "C:\\learnPython\\data\\Iowa.gdb\\Iowa"
 
# Get a list of all feature classes in the USA folder
env.workspace = usa_workspace
featureClass = ListFeatureClasses()

try: 
# Loop through all USA feature classes
    for feature in featureClass:
 
        # Construct the output path
        outClipFeatureClass = "C:\\learnPython\\data\\out_data\\" + str(feature)
 
        # Perform the clip and report what happened
        Clip_analysis(feature, iowa_data, outClipFeatureClass)
        AddMessage("Wrote clipped file " + outClipFeatureClass + ". ")
        print ("Wrote clipped file " + outClipFeatureClass + ". ")

# If happen some error 
except:
    # Show messages for error
    print GetMessages()
