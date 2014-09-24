#-*-coding:utf-8-*-
__author__ = 'shenshen'

import gpxpy
import gpxpy.gpx

def parse(filename):
    gpx_file = open(filename, 'r')
    gpx = gpxpy.parse(gpx_file)
    for track in gpx.tracks:
        print(track.name)
        print(track.description)
        print(track.number)
        for segment in track.segments:
            for point in segment.points:
                print '----Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

    for waypoint in gpx.waypoints:
        print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude)

    for route in gpx.routes:
        print 'Route:'
        for point in route.points:
            print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

    # There are many more utility methods and functions:
    # You can manipulate/add/remove tracks, segments, points, waypoints and routes and
    # get the GPX XML file from the resulting object:

    #print 'GPX:', gpx.to_xml()

if __name__ == '__main__':
    parse('data.gpx')