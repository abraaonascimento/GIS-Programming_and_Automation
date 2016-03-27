# Final Project - Make a census racial map


The objective for this project is make code able to do a census racial map for any city in Brazil, 
in easier and faster way. Normally to do it process manually is hard because of the large amount 
of information involved as long as the different changes that is necessary execute on geographic 
and demographic data. 

With the first version of python code to make a census racial map basically what is necessary to 
do is set the geographic data with geometries of census tract and the demographic data of city or 
states.

### Collecting the data

The Brazilian Institute of Geography and Statistic (IBGE) is the institute responsible to 
production the information about the people in brazil how for example the information the total of
people in each city in Brazil. 

The data used for this example is of Sao Paulo city that can be access in the web sites below, 

- Geographic data: (http://downloads.ibge.gov.br/downloads_estatisticas.htm)
- Gemographic data: ftp://geoftp.ibge.gov.br/malhas_digitais/censo_2010/

### The geographic data

The geographic data of Sao Paulo city is a shapefile with 18.953 geometries of census tract. Normally 
each geometry of census tract has an average of 230 homes or 700 peoples.

####Census track of Sao Paulo city (link)

### The demographic data
The demographic data is a csv file with the information about the ethnicity, gender and age. 
For this example was used only information about ethnicity that are the variables V002 (white people), 
V003 (black people), V004 (yellow people), V005 (parda people) and V006 (indigenous people).

####Sample of demographic data (link)
 

### Using the code

import csv, operator

from arcpy import env, AddField_management, CreateRandomPoints_management , Sort_management
from arcpy.da import UpdateCursor

To make a census racial map is important import the standard functions: csv and operator to work with 
demographic data and the ESRI functions to work with geographic data.

env.workspace = "C:\\demographicMaps\\setores"
It's the line to set the folder with the geometries of census of city or states.

demographicData = open("C:\\demographicMaps\\tabelas\\Pessoa03_SP1.csv")
It's the line for put the csv file with the information about the people.

Now basically what is necessary to do is put the name of geographic file and the name to new geographic 
file. Like below,

geographicData = "sampa"
geographicDataOrder = "sampaOrder"

Is just that, the rest of code is able to make racial map. 

### It's important understand

Each geometry of census tract is identified with one single code. The example below have the code: 
355030845000034. All that is necessary to find the information about the people is just it because it's 
the same code in table by demographic data.
  
One interesting thing for this example this the total number of people: 555. The number of white people: 496. 
The number of pardas people: 40. The number of yellow people: 16. the number of black people: 3 and the 
number indigenous people: 0. 

Each ethnicity have your won shapefile that make a racial map, like below,

Census Racial Map of just one geometry in Sao Paulo city (link)
 
####The same information is also nice to analysis when on one satellite image.


####Census Racial Map of just one geometry in Sao Paulo city (link)
 

 


