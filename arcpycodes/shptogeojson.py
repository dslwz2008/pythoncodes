# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import shapefile
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# read the shapefile
reader = shapefile.Reader("jiashan_lines/jiashan_delete.shp")
fields = reader.fields[1:]
field_names = [field[0].decode('gb2312') for field in fields]
buffer = []
for sr in reader.shapeRecords():
    record = []
    for r in sr.record:
        if type(r) == str:
            record.append(r.decode('gb2312'))
        else:
            record.append(r)
    atr = dict(zip(field_names, record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature",
                       geometry=geom, properties=atr))

# write the GeoJSON file
from json import dumps
# import codecs
geojson = open("jiashan_lines.json", "w")
geojson.write(dumps({"type": "FeatureCollection",
                     "features": buffer}, indent=2) + "\n")
geojson.close()

