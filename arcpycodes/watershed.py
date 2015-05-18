# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import sys
import arcpy
from arcpy import env
from arcpy.sa import *

# usage:
# python watershed.py D:/data/srtm_56_06 flow_direction_raster pour_point_data output.tif pour_point_field(optional)


def main(*args):
    # Set environment settings
    env.workspace = args[1]

    # Set local variables
    inFlowDirection = args[2]
    inPourPointData = args[3]
    inPourPointField = ''
    if len(args) > 4:
        inPourPointField = args[5]

    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")

    # Execute Watershed
    if len(args) > 4:
        outWatershed = Watershed(inFlowDirection, inPourPointData, inPourPointField)
        outWatershed.save(args[4])
    else:
        outWatershed = Watershed(inFlowDirection, inPourPointData)
        outWatershed.save(args[4])


if __name__ == '__main__':
    main(sys.argv)