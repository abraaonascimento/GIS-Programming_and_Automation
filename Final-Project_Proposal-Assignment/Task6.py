#--------------------------------MAKE A RACIAL RANDOW DOT MAP-------------------------------
import csv, operator

from arcpy import env, AddField_management, Sort_management, CreateRandomPoints_management
from arcpy.da import UpdateCursor

# Workspace
env.workspace = "C:\\demographicMaps\\setores"

# Demographic data
demographicData = open("C:\\demographicMaps\\tabelas\\Pessoa03_SP1.csv")
demographicCsv = csv.reader(demographicData, delimiter=";")
demographicCsv.next()
demographicSorted = sorted(demographicCsv, key=operator.itemgetter(0))

# Geographic Data
geographicData = "sampa"

geographicDataOrder = "sampaOrder"
geographicDataTable = geographicDataOrder + ".dbf"

# Create a order geographic data
Sort_management(env.workspace + "\\" + geographicData + ".shp", geographicDataOrder, [["ID", "ASCENDING"]])

# Id census tract
idField = "CD_GEOCODI"

# Position variable of demographic data
valueEt = 2

# New fields to gographich data
newFields = ["white", "black", "yellow", "parda", "indig"]

for field in newFields:

    # Add a new field in table of order geographic data
    AddField_management(geographicDataTable, field, "SHORT", 5)
    valueEt += 1
    print "Creating the field: " + field

    # Upadate the value of demographic data in geographic data
    with UpdateCursor(geographicDataOrder + ".shp", (idField, field)) as geographicRows:

        for geographicRow in geographicRows:

            for demographicRow in demographicSorted:

                if str(geographicRow[0]) == str(demographicRow[0]):

                    try:
                        valueDemographicRow = int(demographicRow[valueEt])
                    except:
                        valueDemographicRow = 0

                    geographicRow[1] = valueDemographicRow
                    geographicRows.updateRow(geographicRow)
                    break

    # Create a randow map
    print "Creating the randow map of " + field + "people"
    CreateRandomPoints_management(env.workspace, field, geographicDataOrder + ".shp", "", field)
    print "The randow map " + field + " was created with sucess!"
