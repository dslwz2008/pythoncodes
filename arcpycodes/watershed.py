# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import sys
import argparse
import arcpy
from arcpy import env
from arcpy.sa import *

# usage: watershed.py [-h] [-ff {NORMAL,FORCE}] [-dr DROP_RASTER]
#                     ws sr xytable out
#
# positional arguments:
#   ws                    specify your workspace.
#   sr                    Raster Layer. The input raster representing a
#                         continuous surface.
#   xytable               The table containing the X and Y coordinates that
#                         define the locations of the point features to create.
#                         Fields must named as follows:x,y,value.
#   out                   Out Raster. The output raster that shows the
#                         contributing area.It will be of integer type.
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -ff {NORMAL,FORCE}, --force_flow {NORMAL,FORCE}
#                         Specifies if edge cells will always flow outward or
#                         follow normal flow rules.
#   -dr DROP_RASTER, --drop_raster DROP_RASTER
#                         Raster Dataset.An optional output drop raster.

# example:
# python watershed.py D:\data\srtm_56_06 srtm_56_06.tif testxy.csv watershed.tif


def watershed(flowDirection, xyLayer, pourPointField, outRaster):
    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")

    # Execute Watershed
    outWatershed = Watershed(flowDirection, xyLayer, pourPointField)
    outWatershed.save(outRaster)


def flowDirection(inSurface, outRaster, forceFlow="NORMAL", outDropRaster=None):
    inSurfaceRaster = inSurface

    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")

    # Execute FlowDirection
    if outDropRaster is None:
        outFlowDirection = FlowDirection(inSurfaceRaster, forceFlow)
        outFlowDirection.save(outRaster)
    else:
        outFlowDirection = FlowDirection(inSurfaceRaster, forceFlow, outDropRaster)
        outFlowDirection.save(outRaster)


def makeXYLayer(table, spref, savedLayer):
    try:
        x_field = "x"
        y_field = "y"
        outLayer = "xyLayerTemp"

        # Make the XY event layer...
        arcpy.MakeXYEventLayer_management(table, x_field, y_field, outLayer, spref)

        # Print the total rows
        # print(arcpy.GetCount_management(outLayer))

        # Save to a layer file
        arcpy.SaveToLayerFile_management(outLayer, savedLayer)
    except:
        # If an error occurred print the message to the screen
        print(arcpy.GetMessages())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ws", help="specify your workspace.")
    parser.add_argument("sr",
                        help="Raster Layer. The input raster representing a continuous "
                             "surface.")
    parser.add_argument("-ff", "--force_flow", choices=["NORMAL", "FORCE"],
                        help="Specifies if edge cells will always flow outward or follow "
                             "normal flow rules.")
    parser.add_argument("-dr", "--drop_raster",
                        help="Raster Dataset.An optional output drop raster.")
    parser.add_argument("xytable",
                        help="The table containing the X and Y coordinates that define "
                             "the locations of the point features to create. Fields must "
                             "named as follows:x,y,value.")
    parser.add_argument("out", help="Out Raster. The output raster that shows the contributing area."
                                   "It will be of integer type.")
    args = parser.parse_args()

    env.workspace = args.ws
    outFlowDirection = "%s/%s" % (env.workspace, "flowDirection.tif")
    if args.force_flow and args.drop_raster: # 同时指定
        flowDirection(args.sr, outFlowDirection, args.force_flow, args.ws)
    elif not args.force_flow and args.drop_raster:
        flowDirection(args.sr, outFlowDirection, outDropRaster=args.drop_raster)
    elif args.force_flow and not args.drop_raster:
        flowDirection(args.sr, outFlowDirection, forceFlow=args.force_flow)
    else:
        flowDirection(args.sr, outFlowDirection)

    spatialRef = arcpy.Describe(args.sr).spatialReference
    # print(spatialRef.exportToString())
    outXyLayer = "%s/%s" % (env.workspace, "xyLayer.lyr")
    makeXYLayer(args.xytable, spatialRef, outXyLayer)

    watershed(outFlowDirection, outXyLayer, "value", args.out)
