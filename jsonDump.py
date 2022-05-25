import os
import json
#import string

def main(filename,output):
	fileModules = open(output,"w")
	modules = []
	resources = []
	total = {}
	output = {}
	cnt = 0
	total_uncom = 0.0
	total_compr = 0.0
	with open(filename) as f:
		## lineloop
		for l in f:
			## avoiding lastline
			try:		
				vl = l.split(" ")
				print(vl)
				## nEvents
				if cnt == 0:
					nEvents = vl[-1].replace("\n","")
					cnt = cnt -1
					continue

				## Normalline discriminator
				disc = vl[1]
				modulesDict = {}
				## Mainline clusters
				if '(' in disc:
					collection = vl[0].replace(":","")
					cl = vl[1]
					size_uncom = vl[-2]
					size_compr = vl[-1].replace("\n","")
					cl = cl.replace("(","").replace(")","")
					modulesDict['events'] = int(nEvents)
					modulesDict['label'] = collection
					### SIZE * nEvents (because of overlapping division) / MB unit
					modulesDict['size_uncom'] = (float(size_uncom)/1048576.)*int(nEvents)
					modulesDict['size_compr'] = (float(size_compr)/1048576.)*int(nEvents)
					modulesDict['type'] = cl
					print(modulesDict)

					## Sum for total
					total_uncom = total_uncom + (float(size_uncom)/1048576.)*int(nEvents)
					total_compr = total_compr + (float(size_compr)/1048576.)*int(nEvents)

				else:
					continue
			
				modules.append(modulesDict)
			except:
				break
		## make resources
		size_uncomDict = {}
		size_comprDict = {}
		size_uncomDict['size_uncom'] = "Average Uncompressed Size"
		size_comprDict['size_compr'] = "Average Compressed Size"
		resources.append(size_uncomDict)
		resources.append(size_comprDict)

		## make total
		total['events'] = nEvents
		total['label'] = "step3_eventsize"
		total['size_uncom'] = total_uncom
		total['size_compr'] = total_compr
		total['type'] = "job"

		## merge modules
		output['modules'] = modules
		output['resources'] = resources
		output['total'] = total
		
		## dump and save
		json.dump(output, fileModules, ensure_ascii=False, indent=4 )

### I/O check
if len(os.sys.argv) < 2:
	print("Missing Input file!!")
	exit(-9)
if len(os.sys.argv) < 3:
	print("Missing Output file!")
	exit(-9)

### define I/O
filename = os.sys.argv[1]
output = os.sys.argv[2]

### main code
if __name__=="__main__":
	main(filename,output)



### EOF
