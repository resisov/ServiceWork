import os
import json
#import string

if len(os.sys.argv) < 2:
	print("Missing Input file!!")
	exit(-9)

filename = os.sys.argv[1]

if __name__=="__main__":
	fileModules = open("module.json","w")
	modulesDict = {}
	with open(filename) as f:
		## lineloop
		for l in f:
			## avoiding lastline
			try:
				vl = l.split(" ")
				collection = vl[0]
				cl = vl[1]

				## only need clusters
				if '(' in cl:
					size = vl[-1]
					modulesDict[collection] = cl
				else:
					continue

				print (collection, cl, size)
			except:
				break

		## dump and save
		json.dump(modulesDict, fileModules, ensure_ascii=False, indent=4 )
