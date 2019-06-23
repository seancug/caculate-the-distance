# -*- coding: utf-8 -*-
import numpy
import pandas


def readdat(filename, head):
    """
    读取数据
    :param filename: 文件名
    :return:
    """
    file_fp = open(filename, 'r')
    list_all_line = file_fp.readlines()
    line_num = 0
    line_lon_lat= []
    linename = []

    for i in range(0, len(list_all_line)):
        line = list_all_line[i]
        tmp = line.split(',')

        if i == len(list_all_line) - 1:
            datasp = list_all_line[i].replace("\r\n", "").split(',')

            latsp = datasp[2].split(':')
            lat2 = float(latsp[0]) + float(latsp[1]) / 60.0 + float(latsp[2]) / 3600.0
            longsp = datasp[3].split(':')
            long2 = float(longsp[0]) + float(longsp[1]) / 60.0 + float(longsp[2]) / 3600.0

            line_lon_lat[line_num - 1].extend([long2, lat2])

        if tmp[0].strip() == head.strip():
            if i > 1:
                datasp = list_all_line[i - 1].replace("\r\n", "").split(',')

                latsp = datasp[2].split(':')
                lat2 = float(latsp[0]) + float(latsp[1]) / 60.0 + float(latsp[2]) / 3600.0
                longsp = datasp[3].split(':')
                long2 = float(longsp[0]) + float(longsp[1]) / 60.0 + float(longsp[2]) / 3600.0

                line_lon_lat[line_num - 1].extend([long2, lat2])

            datasp = list_all_line[i + 1].replace("\r\n", "").strip('\n').split(',')

            latsp = datasp[2].split(':')
            lat1 = float(latsp[0]) + float(latsp[1]) / 60.0 + float(latsp[2]) / 3600.0
            longsp = datasp[3].split(':')
            long1 = float(longsp[0]) + float(longsp[1]) / 60.0 + float(longsp[2]) / 3600.0

            line_lon_lat.append([long1, lat1])
            linename.append(tmp[2])
            line_num += 1
    return linename, line_lon_lat

def writehtml(filename, index, datain):
    """输出数据"""
    data_df = pandas.DataFrame(data=datain.T, index=index, columns=['Distance'])
    data_df.to_csv(filename + '.csv')
    data_df.to_html(filename + '.html')

def rad(d):
    return d * numpy.pi / 180.0

def calc_distance(lon_lat):
    """
    :param lon1:第一点经度
    :param lat1:第一点纬度
    :param lon2:第二点经度
    :param lat2:第二点纬度
    :return:两点距离
    """
    EARTH_RADIUS = 6371.004

    lon_lat = numpy.array(lon_lat)
    lon_lat = rad(lon_lat)

    x1 = numpy.cos(lon_lat[:, 1]) * numpy.cos(lon_lat[:, 0])
    x2 = numpy.cos(lon_lat[:, 3]) * numpy.cos(lon_lat[:, 2])
    y1 = numpy.cos(lon_lat[:, 1]) * numpy.sin(lon_lat[:, 0])
    y2 = numpy.cos(lon_lat[:, 3]) * numpy.sin(lon_lat[:, 2])
    z1 = numpy.sin(lon_lat[:, 1])
    z2 = numpy.sin(lon_lat[:, 3])

    delta = x1 * x2 + y1 * y2 + z1 * z2

    return numpy.round(numpy.arccos(delta) * EARTH_RADIUS, 1)