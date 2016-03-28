# Making a census racial dot map


The main goal for this project is make the code able to perform a census racial dot map for any city in Brazil, 
in easier and faster way. Because of the large amount of information involved in this process, 
and the both diverse geographic and demographic data, it is not recommended to perform it manually.

With this version of code, it is possible to create a census racial dot map for any city in Brazil. Basically what you need to do
is to set the geographic data with geometries of census tract and the demographic data with variables for census tract.

### Collecting the data

The Brazilian Institute of Geography and Statistic (IBGE) is the institute responsible to 
collect and assemble the information about the people in Brazil. For example, the total of
population on a certain area or city. 

The data used for this example is the data of Sao Paulo city and it can be accessed in the web sites below, 

- Geographic data: 
  - http://downloads.ibge.gov.br/downloads_estatisticas.htm
- Demographic data: 
  - ftp://geoftp.ibge.gov.br/malhas_digitais/censo_2010/

### The geographic data

The geographic data of Sao Paulo city it is a shapefile with 18.953 geometries of census tract. Normally 
each geometry of census tract has an average of 230 homes or 700 peoples.

#####Census track of Sao Paulo city
![sample censu sampa](http://i.imgur.com/4GzK7SX.png)

### The demographic data
The demographic data it is a csv file with the information about the ethnicity, gender and age. 
For this example was used only information about ethnicity. It's the variables V002 (white people), 
V003 (black people), V004 (yellow people), V005 (parda people) and V006 (indigenous people).

#####Sample demographic data
![sample demogrphic data sampa](http://i.imgur.com/WWWpSwx.png)

### Using the code

``import csv, operator``

``from arcpy import env, AddField_management, CreateRandomPoints_management , Sort_management``
``from arcpy.da import UpdateCursor``

To make a census racial dot map is necessary import the standard functions of python: **csv** and **operator** to work with 
demographic data and the ESRI functions: **env, AddField_management, CreateRandomPoints_management , Sort_management** to work with geographic data.

``env.workspace = "C:\\demographicMaps\\setores"``
It's the line to set the folder with the geometries of census of city or state.

``demographicData = open("C:\\demographicMaps\\tabelas\\Pessoa03_SP1.csv")``
It's the line for put the csv file with the information about the people.

Now, basically what is necessary to do is put the name of geographic data (shapefile). As below,

``geographicData = "sampa"``

Is just that, the rest of code in **Task6.py** is able to make a racial dot map. 

### It's important understand

Each geometry of census tract is identified with one single code. The example below have the code: 
355030845000034. All that is necessary to find the information about the people is just it code, because it's 
the same code in table by demographic data.

![census geometry sampa](http://i.imgur.com/w5ASJ7Z.png)
  
One interesting thing for this example is the total number of people: 555. The number of white people: 496. 
The number of parda people: 40. The number of yellow people: 16. the number of black people: 3 and the 
number indigenous people: 0. 

Each ethnicity have your won shapefile that create a racial dot map. As seen in, 

#####Census racial dot map of just one geometry in Sao Paulo city
![census geometry sampa](http://i.imgur.com/6Lvwdyx.png)
 
The same information is also nice to analysis when it's on one satellite image.

#####Census racial dot map of just one geometry in Sao Paulo city
![census geometry sampa](http://i.imgur.com/n2Q6IYC.jpg)
