# -*- coding: utf-8 -*-
import sys, os
import calc_distance.calc_distance as cd

print '''Example: main datain.dat BHX2017 dataout\n参数:\n\
datain.dat:\t输入文件名\nBHX2017:\t导航头文行首字符\ndataout:\t输出文件'''

if len(sys.argv) !=4 :
    print ''
    print "函数参数输入不正确"
    exit(-1)
if not os.path.exists(sys.argv[1]):
    print ''
    print "%s File Does Not Exists" %(sys.argv[1])
    exit(-2)

line, datain = cd.readdat(sys.argv[1],sys.argv[2])
distance = cd.calc_distance(datain)
cd.writehtml(sys.argv[3], line, distance)
print ''
print "总测线数：%d\t" %(len(line))
print "输入文件名：%s\t" %(sys.argv[1])
print "输出文件名：%s\t" %(sys.argv[3]+'.csv'+'\t'+sys.argv[3]+'.html')