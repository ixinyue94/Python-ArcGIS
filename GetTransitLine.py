#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python版本-ArcGIS自带

import arcpy
from arcpy import  da
from arcpy import  env
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
env.overwriteOutput = True

#新建线要素
path = 'F:\\test\\'                 # 设置公交shp文件生成路径
shp_output = path + 'bus.shp'       # 设置公交shp文件名称

arcpy.CreateFeatureclass_management(os.path.dirname(shp_output), os.path.basename(shp_output), 'POLYLINE', "","","",spatial_reference= 4326)
arcpy.AddField_management(shp_output, 'name', 'Text')
arcpy.AddField_management(shp_output, 'startTime', 'Text')
arcpy.AddField_management(shp_output, 'endTime', 'Text')
arcpy.AddField_management(shp_output, 'num', 'Text')
arcpy.AddField_management(shp_output, 'company', 'Text')
fields = ['SHAPE@', 'name','startTime','endTime','num', 'company']

array = arcpy.Array()
cur = da.InsertCursor(shp_output, fields)
with open(r'***.txt', "r") as f:    # 设置html返回数据转换坐标系后的数据存储路径，参考示例-new.txt文件格式
    for line in f.readlines():
        line = line.strip('\n').split(';')
        name = line[0]
        startTime = line[1]
        endTime = line[2]
        numStations = line[3]
        company = line[4]
        path = line[5:]
        for i in range(0, len(path)):
            xy = path[i].split(',')
            x = xy[0]
            y = xy[1]
            pnt = arcpy.Point(x,y)
            array.add(pnt)
        polyline = arcpy.Polyline(array, 4326)
        array.removeAll()
        newFields = [polyline, name, startTime, endTime, numStations, company]
        cur.insertRow(newFields)
