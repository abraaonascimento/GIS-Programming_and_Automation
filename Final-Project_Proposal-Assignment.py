#-----------------------------------------------------------------------
import csv, operator
 
# Taks 1 - make a randow point shapefile

"""
shp = "C:\\demographicMaps\\setores\\randowTeste.shp"
out = "C:\\demographicMaps\\setores"
arcpy.CreateRandomPoints_management(out, "randowPeople", shp, "", "point")
"""

#from arcpy import env, CreateRandomPoints_management, UpdateCursor, Sort_management

#env.workspace = "C:\\demographicMaps\\setores"

# Task 2 - order CSV

"""
demographicData = open("C:\\demographicMaps\\tabelas\\Pessoa03_SP1.csv")
demographicCsv = csv.reader(demographicData, delimiter=";")

sortedlist = sorted(demographicCsv, key=operator.itemgetter(0))
"""

# Task 3 - show the first row for each field that you'll use

"""
for row in demographicCsv:
	print row #show everybody of first line
	print row[0] #show the cesus code
	print row[3] #show tha value of variable V002 ----> cor branca
	print row[4] #show tha value of variable V003 ----> cor preta
	print row[5] #show tha value of variable V004 ----> cor amarela
	print row[6] #show tha value of variable V005 ----> cor parda
	print row[6] #show tha value of variable V006 ----> cor indigina
	break
"""


# Task 4 - create a new field in geographic data and update the value of first row
"""
from arcpy import env, AddField_management, Sort_management
from arcpy.da import UpdateCursor

env.workspace = "C:\\demographicMaps\\setores"

geographicData = "sampa"
geographicDataOrder = "sampaOrder"
geographicDataTable = "sampaOrder.dbf"

Sort_management("C:\\demographicMaps\\setores\\sampa.shp", geographicDataOrder, [["ID", "ASCENDING"]])

newField = "brancos"

AddField_management(geographicDataTable, newField, "TEXT", 100)

with UpdateCursor(geographicDataOrder + ".shp", newField) as geographicRows:

    for row in geographicRows:

        # Update the value for each row in typeAmenities
        row[0] = "value for white people"
        geographicRows.updateRow(row)
"""

# Task 5 - Update de value of each row of csv in geographic data
import csv, operator

from arcpy import env, AddField_management, Sort_management
from arcpy.da import UpdateCursor


env.workspace = "C:\\demographicMaps\\setores"
geographicDataOrder = "sampaOrder"
whiteField = "brancos"
idField = "CD_GEOCODI"

demographicData = open("C:\\demographicMaps\\tabelas\\Pessoa03_SP1.csv")
demographicCsv = csv.reader(demographicData, delimiter=";")
demographicCsv.next()
demographicSorted = sorted(demographicCsv, key=operator.itemgetter(0))
count = 0
# Put the code census field
with UpdateCursor(geographicDataOrder + ".shp", (whiteField, idField)) as geographicRows:    

    for geographicRow in geographicRows:

        for demographicRow in demographicSorted:

            #print geographicRow[0]
            #print geographicRow[1]
            #print demographicRow[0]
            #break
            #break
            # da erro por causa do indice que ficou como ultimo registro, acho que um next no demographicCsv  já funciona
            if str(geographicRow[1]) == str(demographicRow[0]):
                print geographicRow[1]
                idDemographicRow = str(demographicRow[3]) # 3 == v002
                geographicRow[0] = idDemographicRow
                    
                count += 1

            # Update the value for each row in typeAmenities
                #row[0] = demographicRow[3]
                geographicRows.updateRow(geographicRow)

"""
geographicData = "sampa"
geographicDataOrder = "sampaOrder2"

codSetorField = "ID"

queryOrderByDesc = "ORDER BY A"


Join dont works.

Do update of values in aech row in layer 
"""

#Sort_management("C:\\demographicMaps\\setores\\sampa.shp", geographicDataOrder, [[codSetorField, "ASCENDING"]])

#with UpdateCursor(demographicData, codSetorField, {queryOrderByDesc}) as demographicRows:
    
        #for row in demographicRows:
            
         #   lineRow = row[0]

          #  print lineRow


#---------------STEPS

# Ordenar os ids

        # demographicData
        # geographicData


# Two ways

    # primeiro

        # Relacioanar cada registro da tabela de setores com a tabela de shapefile
        # Para cada relação checar a coluna de referencia (origem dos dados) como por exemplo a quantidade de pessoas pardas
        # Para cada coluna idenfificar o valor do resgistro
        # Em cada volor de registro (por coluna) gerar um mapa de pontos aleatórios dentro da geometria dos poligonos
        # Quardar cada uma das informações atribuir a unico shapefile

    # segundo

        # fazer um join espacial pela codigo do setor
        # para cada coluna de interesse gerar pontos aleatorios por coluna dado o valor de cada registro
        # Cada ponto gerado precisa ter um identificado (nesse caso o nome da coluna)

# Produto final

    # two ways

        # first

            # shape de pontos aleatorios dentro de cada geometria do poligono correspondente,
            # cada ponto gerado precisa ter o nome da coluna associado a ele
            # pois assim conseguimos conseguimos gerar mapas para cada tipo de variavel selecionada

        # second

            # gerar um shape serado para cada coluna.
            # Nesse caso o nome da coluna pode ser associada somente ao nome do shapefile
            # isso descarta a obrigação de ter cada resgistro/ponto gerado o nome da coluna associado

# Fazer um esquema funcional
#mas depois pensar em algo mais cabeça
#para que seja possível gerar diferentes
#tipos de mapas com a mesma funcionalidade


#CreateRandomPoints_management 
