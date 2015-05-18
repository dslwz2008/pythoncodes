# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import sys
import arcpy
from arcpy import env

class LicenseError(Exception):
    pass

# usage:
# python testarcpy.py "D:/data/srtm_56_06" "Aspect_3d" "srtm_56_06.tif" "testaspect.tif"
# args index :   0          1                   2           3                   4
# python testarcpy.py "D:/data/srtm_56_06" "Slope_3d" "srtm_56_06.tif" "testslope.tif" "DEGREE" 0.3043

def main(*args, **kwargs):
    try:
        if arcpy.CheckExtension("3D") == "Available" or \
                arcpy.CheckExtension("GeoStats") == "Available" or \
                arcpy.CheckExtension("Network") == "Available" or \
                arcpy.CheckExtension("Spatial") == "Available" or \
                arcpy.CheckExtension("Tracking") == "Available":
            arcpy.CheckOutExtension("3D")
            arcpy.CheckOutExtension("GeoStats")
            arcpy.CheckOutExtension("Network")
            arcpy.CheckOutExtension("Spatial")
            arcpy.CheckOutExtension("Tracking")
        else:
            raise LicenseError

        # Set environment settings
        env.workspace = args[0][1]
        func = eval("arcpy." + args[0][2])
        # Execute
        print(u'正在计算，请稍后...')
        func(*args[0][3:])
        print(u'计算完毕！')
    except LicenseError:
        print("license is unavailable")
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
    finally:
        # Check in the ArcGIS 3D Analyst extension
        #
        arcpy.CheckInExtension("3D")
        arcpy.CheckInExtension("GeoStats")
        arcpy.CheckInExtension("Network")
        arcpy.CheckInExtension("Spatial")
        arcpy.CheckInExtension("Tracking")


if __name__ == '__main__':
    main(sys.argv)