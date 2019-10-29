import arcpy
import os.path

path1 = 'stops'
path2 = 'lines'

path_stop = []
path_line = []
f1 = os.listdir(path1)
f2 = os.listdir(path2)

for i in f1:
if i[-3:] == 'shp':
path_stop.append(path1 + '/' + i)
for j in f2:
if j[-3:] == 'shp':
path_line.append(path2 + '/' + j)

for n in range(0,190):
infc = path_stop[n]
line = path_line[n]
print infc
arcpy.Near_analysis(infc, line, "", "true")
