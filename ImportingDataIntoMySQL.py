#!/bin/python3
# generate script for importing data into MySQL


country = input("what country?")
crop = input("what crop?")

fout = open("/home/johan/Documents/Work/CropDST/apsim/outFileData/importScript.txt", 'w')

fout.write("In the terminal: \n")
fout.write("\n")
fout.write("cd /home/johan/Documents/Work/CropDST/apsim/outFileData/\n")
fout.write("sed 's/ \+/ /g' outData"+country+crop+".csv > "+crop+country+".csv\n")

fout.write("head "+crop+country+".csv\n")
fout.write("\n")

fout.write("In MySQL\n")
fout.write("\n")
fout.write("CREATE TABLE "+crop+country+" LIKE "+crop+"ZWE;\n")
if crop != "bean":
	fout.write("ALTER TABLE "+crop+country+" MODIFY Date VARCHAR(10);\n")

fout.write("LOAD DATA LOCAL INFILE '/home/johan/Documents/Work/CropDST/apsim/outFileData/"+crop+country+".csv'\n")
fout.write("INTO TABLE "+crop+country+"\n")
fout.write("FIELDS TERMINATED BY ' '\n")
fout.write("LINES TERMINATED BY '\\n'\n")
fout.write("IGNORE 1 LINES\n")
if crop == "cowpea":
	fout.write("(metGrid,cultivar,soil,year,sumRain,rainClass,@var1,day, yearDupl, cropYield, weedYield,cowpeaBiomass,weedBiomass)\n")
elif crop == "bean":
	fout.write("(metGrid,cultivar, soil, year, sumRain, rainClass, day, yearDupl, weedYield, cropYield, weedBiomass, navybeanBiomass);\n")
elif crop == "soybean":
	fout.write("(metGrid, cultivar, soil, year, sumRain, rainClass, @var1, day, yearDupl, cropYield, weedYield, cropBiomass, weedBiomass)\n")
elif crop == "maize":
	fout.write("(metGrid, cultivar, soil, fertiliser, year, sumRain, rainClass, @var1, day, yearDupl, weedYield, cropYield, weedBiomass, maizeBiomass)\n")
elif crop == "sorghum":
	fout.write("(metGrid, cultivar, soil, fertiliser, year, sumRain, rainClass, @var1, esw, day, yearDupl, weedYield, cropYield, weedBiomass, sorghumBiomass)\n")	
	
if crop != "bean":
	fout.write("SET Date = STR_TO_DATE(@var1, '%d/%m/%Y');\n")
	fout.write("ALTER TABLE "+crop+country+" MODIFY Date DATE;\n")
fout.write("SELECT * FROM "+crop+country+" LIMIT 10;\n")
fout.write("\n")
fout.close()
