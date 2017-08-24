#!/usr/bin/env python
# python3
# -*- coding: utf-8 -*-
#
#  agmerraMetFiles.py
#  make .met files based on the Agmerra data
#
#  Copyright 2016 johan <johan.ecotopic@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

from os import walk
from os import path
from os import makedirs

import datetime




def lineCount(textFile):
	size=0
	with open(textFile,'r') as f:
		size = sum(1 for _ in f)
	f.close()	
	return size

def listOfFiles2(workbookFile):
	fileList = []
	lines=lineCount(workbookFile)
	with open(workbookFile,'r') as f:
		for l in range(lines):
			fileList.append(f.readline()[:11])
	f.close()	
	return fileList


def listOfFiles(workbookDir):
	fileList = []
	for (root, dirpath, files) in walk(workbookDir):
		for f in files:
			fileList.append(root+'/'+f)
	return fileList

country='MDG'	
workbookDir = '/home/johan/Documents/Work/CropDST/DataSource/AgmerraData/AgMERRA_SSA/'
#workbookDir = '/home/johan/Dropbox/CropDST/Rainfall/Agmerra/data'
#workbookFile = '/home/johan/Dropbox/johan/scripts/python/RSA300mm.csv'
workbookFile = '/home/johan/Documents/Work/CropDST/agmerra/agmerra%s.csv'%country
#workbookFile = '/home/johan/Documents/Work/CropDST/agmerra/agmerraBotswana_300MM.csv'
#workbookList = listOfFiles(workbookDir)
workbookList = listOfFiles2(workbookFile)

#print(workbookList)
#for wb in workbookList:
#	print(wb[:7])


#fout = open('/home/johan/Documents/Work/CropDST/agmerra/avgSumRainData.txt', 'w')
#fout.write("STATION  avgRAIN\n")
for wb in workbookList:
	try:
		fileName = wb[:7]
		wb = workbookDir+fileName+'.WTH'
	#	wb = "/home/johan/Documents/Work/CropDST/DataSource/AgmerraData/%s" %(wb)
		lines = lineCount(wb)
	#	print ("Number of lines in",wb,":",lines)
		if not path.exists("/home/johan/Documents/Work/CropDST/agmerra/MET_%sgrids"%country):
			makedirs("/home/johan/Documents/Work/CropDST/agmerra/MET_%sgrids"%country)
		fout = open("/home/johan/Documents/Work/CropDST/agmerra/MET_%sgrids/%s.met" %(country,fileName), 'w')
		with open(wb,'r') as f:
			fout.write("[weather.met.weather]\n")
			next(f)
			next(f)
			line=f.readline().split()
			fout.write("latitude= "+line[1]+"\n")
			fout.write("!%s" %(fileName)) 
	#		print("station:",station)
			fout.write("\n")
			fout.write("\n")
			fout.write("\n")
			now=datetime.datetime.now()
			date=str(now.day)+"/"+str(now.month)+"/"+str(now.year)
			time=str(now.hour)+":"+str(now.minute)
			fout.write("   ! TAV and AMP inserted from agmerraSSA on "+date+" at "+time+" for period from 1980 to 2010\n")
			fout.write(" tav =   "+line[4]+" (oC)     ! annual average ambient temperature\n")
			fout.write(" amp =   "+line[5]+" (oC)     ! annual amplitude in mean monthly temperature\n")
			fout.write("\n")
			fout.write("year    day     radn    maxt    mint    rain\n")
			fout.write("()      ()      (MJm^2) (oC)    (oC)    (mm)\n")
			next(f)
			for l in range(lines-4):
				# read each line, split it and write the components to fout
				line = f.readline().split()
	#			print(int(line[0][:2]))
				if int(line[0][:2])>11:
					fout.write("    19"+line[0][:2]+"     "+line[0][2:])
				elif int(line[0][:2])<11:
					fout.write("    20"+line[0][:2]+"     "+line[0][2:])
				fout.write("  "+line[1].rjust(4," ")+"   "+line[2].rjust(4," ")+"   "+line[3].rjust(4," ")+"   " +line[4].rjust(4," ")+"\n")
			f.close()
		fout.close()
		with open('/home/johan/Documents/Work/CropDST/agmerra/%s_metGrids.txt'%country, 'a') as file:
			file.write('%s\n'%wb)
	except:
		with open('/home/johan/Documents/Work/CropDST/agmerra/%s_missingGrids.txt'%country, 'a') as file:
			file.write('%s\n'%wb)
	
