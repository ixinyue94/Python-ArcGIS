#!/usr/bin/python 
# -*- coding: utf-8 -*-
# 行政区搜索POI（适用于搜索区域内的POI数量不超过400个）
# 服务文档http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi

#代码开始
import requests
f = open(r'H:\江宁公交站.txt', 'a')  #设置数据保存位置

baidu = 'http://api.map.baidu.com/place/v2/search?output=json&page_size=20&coord_type=1'
ak = '***'   #申请的密钥 http://lbsyun.baidu.com/apiconsole/key/create  
q = '公交站'  #设置POI名称
region = '南京市江宁区'  #设置搜索区域

def get_page_num(r):  #获取返回数据的总页码，每页20个数据
    url1 = baidu + '&q=' + q + '&region=' + r + '&ak=' + ak + '&page_num=0'
    total = requests.get(url1).json()['total']
    print('该区域共有 ' + str(total) + ' 个'+ q)
    if total > 0:
        pages = int(total / 20) + 1
        return pages
    else:
        return 0

def get_poi(r, p):  #获取并保存每页中每项数据的名称、纬度、经度
        url2 = baidu + '&q=' + q + '&region=' + r + '&ak=' + ak + '&page_num=' + str(p)
        response = requests.get(url2).json()
        for i in response['results']:
            name = i['name']
            lat = i['location']['lat']
            lng = i['location']['lng']
            bus = name + ',' + str(lat) + ',' + str(lng)
            print(bus)
            f.write(bus + '\n') 

if __name__ == '__main__':
    for p in range(0, get_page_num(region)):
        get_poi(region, p)
