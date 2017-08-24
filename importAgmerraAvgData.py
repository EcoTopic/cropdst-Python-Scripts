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
#workbookFile = '/home/johan/Documents/Work/CropDST/agmerra/agmerra%s.csv'%country
#workbookFile = '/home/johan/Documents/Work/CropDST/agmerra/agmerraBotswana_300MM.csv'
#workbookList = listOfFiles(workbookDir)
workbookFile = '/home/johan/Documents/Work/CropDST/agmerra/list_tables.txt'
workbookList = listOfFiles2(workbookFile)

#print(workbookList)
#for wb in workbookList:
#	print(wb[:7])


#fout = open('/home/johan/Documents/Work/CropDST/agmerra/avgSumRainData.txt', 'w')
#fout.write("STATION  avgRAIN\n")
count = 1
totalLines = lineCount(workbookFile)
for wb in workbookList:
		fileName = wb[:7]
		wb = workbookDir+fileName+'.WTH'
		#lines = lineCount(wb)
		#print ("Number of lines in",wb,":",lines)
		fout = open("/home/johan/Documents/Work/CropDST/agmerra/agmerraAVG_Data.csv", 'a')
		with open(wb,'r') as f:
			next(f)
			next(f)
			line = f.readline().split()
			fout.write(fileName)
			fout.write(" "+line[0]+" "+line[1].rjust(4," ")+" "+line[2].rjust(4," ")+" " +line[3].rjust(4," ")+" " +line[4].rjust(4," ")+" "+line[5].rjust(4," ")+" " +line[6].rjust(4," ")+" "+line[7].rjust(4," ")+"\n")
			f.close()
			print("Processed file ",count," of ",totalLines)
			count +=1
		fout.close()
