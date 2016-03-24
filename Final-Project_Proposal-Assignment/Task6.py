# Taks 6 - Create all colum to racil map. You need this: # white, # black, # yellow, # parda, # indigenous
# and update de correct values for each colum ethnicity
import csv, operator

from arcpy import env, AddField_management, Sort_management
from arcpy.da import UpdateCursor

demographicData = open("C:\\demographicMaps\\tabelas\\Pessoa03_SP1.csv")
demographicCsv = csv.reader(demographicData, delimiter=";")
demographicCsv.next()
demographicSorted = sorted(demographicCsv, key=operator.itemgetter(0))

env.workspace = "C:\\demographicMaps\\setores"

geographicData = "sampa"
geographicDataOrder = "sampaOrder"
geographicDataTable = "sampaOrder.dbf"

Sort_management("C:\\demographicMaps\\setores\\sampa.shp", geographicDataOrder, [["ID", "ASCENDING"]])

idField = "CD_GEOCODI"
newFields = ["white", "black", "yellow", "parda", "indigenous"]
valueEt = 2

for field in newFields:

    AddField_management(geographicDataTable, field, "TEXT", 100)
    valueEt += 1
    
    with UpdateCursor(geographicDataOrder + ".shp", (idField, field)) as geographicRows:

        for geographicRow in geographicRows:

            for demographicRow in demographicSorted:
                    

                if str(geographicRow[0]) == str(demographicRow[0]):

                    # See -----> if demographicRow[0] == "NULL":

                        valueDemographicRow = "0"
                else:

                    print geographicRow[0]
                    valueDemographicRow = str(demographicRow[valueEt]) # 3 == v002
                    geographicRow[1] = valueDemographicRow
                    
                    geographicRows.updateRow(geographicRow)

                    break
