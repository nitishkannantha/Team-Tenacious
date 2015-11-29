#!/usr/env/python

"""
Intent of the code is to find frauds, a very rudimentary manner though

USAGE:

python fraud.py dataset_1gb.csv frauds.csv - a hive equivalent basically

"""

import sys

datafile = sys.argv[1]

fraudjson = {}

with open(datafile, "r") as data:
	for line in data:
		cols = line.split(',')
		deviceid = cols[16]
		deviceip = cols[17]
		outcome = cols[28]

		if deviceid not in fraudjson.keys():
			fraudjson[deviceid]={}
			fraudjson[deviceid]['cnt']=1
			fraudjson[deviceid]['ip_cnt']=0
			if outcome == 'C' or outcome == 'c':
				fraudjson[deviceid]['click'] = 1
			else:
				fraudjson[deviceid]['click'] = 0
			if deviceip not in fraudjson[deviceid].keys():
				fraudjson[deviceid][deviceip]={}
				fraudjson[deviceid]['ip_cnt']=fraudjson[deviceid]['ip_cnt']+1
		else:
			fraudjson[deviceid]['cnt']=fraudjson[deviceid]['cnt']+1
			if outcome == 'C' or outcome == 'c':
				fraudjson[deviceid]['click'] = fraudjson[deviceid]['click'] + 1
			if deviceip not in fraudjson[deviceid].keys():
				fraudjson[deviceid][deviceip]={}
				fraudjson[deviceid]['ip_cnt']=fraudjson[deviceid]['ip_cnt']+1
for key in fraudjson.keys():
	cnt = fraudjson[key]['cnt']
	click = fraudjson[key]['click']
	ip_cnt = fraudjson[key]['ip_cnt']

	ip_ratio = float(ip_cnt)/float(cnt)
	click_ratio = float(click)/float(cnt)

	if cnt > thresh_cnt:
		if click_ratio > thresh_click and ip_ratio > thresh_ip:
			print "device id: "+str(key)+" could be a fraud. anomaly found!"
			print "[INFO]: deviceid: "+str(deviceid)
			print "[INFO]: occurence: "+str(cnt)
			print "[INFO]: clicks: "+str(click)
			print "[INFO]: distinct ips: "+str(ip_cnt)
			print "==================================="



