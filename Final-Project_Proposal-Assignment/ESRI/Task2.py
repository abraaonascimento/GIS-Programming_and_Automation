# --------------------- TASK 2 - MAKE A ORDER CSV --------------------------
import csv, operator

# Setting the csv file
demographicData = open("C:\\demographicMaps\\tabelas\\Pessoa03_SP1.csv")

# Read the csv file
demographicCsv = csv.reader(demographicData, delimiter=";")

# Skips the indexPass the index
demographicCsv.next()

# Order the csv file
sortedlist = sorted(demographicCsv, key=operator.itemgetter(0))
