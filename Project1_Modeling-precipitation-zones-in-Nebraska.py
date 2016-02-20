from arcpy import env, Clip_analysis, ListFeatureClasses, RasterToPolygon_conversion
from arcpy.sa import Idw

# The path to folder with shapefiles
folder_shapefiles = "C:/learnPython/GIS-automation/data"

# Setting workspace
env.workspace = folder_shapefiles

# Shapefiles
shape_point = "Precip2008Readings"
shape_polygon = "Nebraska"

def precipitation_map_Nebraska(shape_point, shape_polygon):
    """
    This function use four modules of Arcpy to create a vector file 
    with different zones of precipitation in Nebraska
    """
    
    # Using the function Idw for determine the inverse distance weighted
    idw_map = Idw(name_shape_point, "RASTERVALU")

    # Using the function Reclassify for to do the reclassification the map of inverse distance weighted
    reclass_map = Reclassify(idw_map, "Value", RemapRange([[0,30000,1],[30000,60000,2],
                                                           [60000,90000,3],[90000,120000,4]]))

    # Transforming file raster to polygon
    out_shapefile = "map_precipitation1"
    raster_to_polygon = arcpy.RasterToPolygon_conversion(reclass_map, folder_shapefiles + "/" + out_shapefile,
                                                         "NO_SIMPLIFY","VALUE")
    
    # Using the function Clip_analysis for create vector polygons with different zones in Nebraska
    out_shapefile_precipitation = "Nebraska_precipitation"
    Nebraska_precipitation = Clip_analysis(out_shapefile, shape_polygon,
                                           folder_shapefiles + "/" + out_shapefile_precipitation)


def main():

    # Create shapefile for map precipitation in Nebraska
    precipitation_Nebraska(shape_point, shape_polygon)

if __name__ == "__main__":
    main()
