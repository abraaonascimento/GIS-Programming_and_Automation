#-----TASK 4 - CREATE A NEW FIELD IN GEOGRAPHIC DATA AND UPDATE THE VALUE OF FIRST ROW----

from arcpy import env, AddField_management
from arcpy.da import UpdateCursor

# Setting the workspace
env.workspace = "C:\\demographicMaps\\setores"

# Setting the geographic data
geographicData = "sampa"
geographicDataTable = "sampa.dbf"

# The name of new field
newField = "white"

# Create the new field in table of geographic data
AddField_management(geographicDataTable, newField, "TEXT", 100)

with UpdateCursor(geographicDataOrder + ".shp", newField) as geographicRows:

    for row in geographicRows:

        # Update the value for each row in newField
        row[0] = "white people"
        geographicRows.updateRow(row)
