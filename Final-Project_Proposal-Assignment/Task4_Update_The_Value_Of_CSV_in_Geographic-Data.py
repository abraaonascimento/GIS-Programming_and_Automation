#---------------TASK 4 - UPDATE THE VALUE OF GEOGRAPHIC DATA WITH EACH VALUE OF CSV------------- 
import csv, operator

from arcpy import env
from arcpy.da import UpdateCursor

# Setting the workspace
env.workspace = "C:\\demographicMaps\\setores"

# Setting the geographic data
geographicDataOrder = "sampaOrder"

# Setting the name of fields
whiteField = "white"
idField = "CD_GEOCODI"

# Setting the demographic data (csv)
demographicData = open("C:\\demographicMaps\\tabelas\\Pessoa03_SP1.csv")
demographicCsv = csv.reader(demographicData, delimiter=";")

# Skip the index and order the csv
demographicCsv.next()
demographicSorted = sorted(demographicCsv, key=operator.itemgetter(0))

# Update the value of geographic data with each data in csv
with UpdateCursor(geographicDataOrder + ".shp", (whiteField, idField)) as geographicRows:    

    # Walks for each row in geographic data and each row in csv
    for geographicRow in geographicRows:
        for demographicRow in demographicSorted:

            # Check if the code area of geographic data is equal the code area of demographic data
            if str(geographicRow[1]) == str(demographicRow[0]):
            
                # Write the value of csv in geographic data
                idDemographicRow = str(demographicRow[3]) # The value in location 3 is the value of white people in census area 
                geographicRow[0] = idDemographicRow
                
                # Salve the changes
                geographicRows.updateRow(geographicRow)
                
                # break the loop and pass to the next row
                break
