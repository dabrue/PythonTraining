#!/usr/bin/python 
import math
import numpy
import sys
import os

# Define sphere radius
Earth_Mean_Radius = 6371009  # meters
Earth_Min_Radius  = 6353000  # meters
Earth_Max_Radius  = 6384000  # meters
Earth_Polar_Radius = 6356752.3  # meters
Earth_Equatorial_Radius = 6378137.0 # meters
Radius = Earth_Mean_Radius

pi=math.pi
pi2=math.pi/2.0

meters_to_miles = 0.000621371

# Read in two sphere surface points
f=open(sys.argv[1],"r")

# Each line in the file should have 8 fields, describing two points on the surface of the 
# earth. 
# Latitude  Longitude Latitude  Longitude 
# for Latitude, positive is NORTH, negative is SOUTH
# for Longitude, positive is EAST, negative is WEST
fpts=f.readlines()

# Convert each pair of points into pairs of vectors
for i in range(len(fpts)):
    fpts[i]=fpts[i].rstrip("\n")
    sdata=fpts[i].split()
    if (len(sdata) != 4):
        print "ERROR: expected 4 numbers, line:", i+1
        exit()
    lat0=float(sdata[0])*pi2/90.0
    lon0=float(sdata[1])*pi2/90.0
    lat1=float(sdata[2])*pi2/90.0
    lon1=float(sdata[3])*pi2/90.0
    vec0=numpy.zeros(3)
    vec1=numpy.zeros(3)
    vec0[0] = math.cos(lon0)*math.sin(pi2-lat0)
    vec0[1] = math.sin(lon0)*math.sin(pi2-lat0)
    vec0[2] = math.cos(pi2-lat0)
    vec1[0] = math.cos(lon1)*math.sin(pi2-lat1)
    vec1[1] = math.sin(lon1)*math.sin(pi2-lat1)
    vec1[2] = math.cos(pi2-lat1)
    test0=numpy.dot(vec0,vec0)
    test1=numpy.dot(vec1,vec1)
    dot_product = numpy.dot(vec0, vec1)
    theta = math.acos(dot_product)
    dist=theta*Radius
    theta=theta*90/pi2
    dot_str=str(dot_product).ljust(20)
    theta_str = str(theta).ljust(20)
    dist_str = str(dist).ljust(20)
    miles_str=str(dist*meters_to_miles).ljust(20)
    print dot_str, theta_str, dist_str, miles_str

