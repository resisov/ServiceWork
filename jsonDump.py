import os
import json

if len(os.sys.argv) < 2:
	print("Missing Input file!!")
	exit(-9)

filename = os.sys.argv[1]

if __name__=="__main__":
	fileModules = open("test.json","w")
	modulesDict = {}
	with open(filename) as f:
		for l in f:
			try:
				vl = l.split(" ")
				collection = vl[0]
				cl = vl[1]
				size = vl[-1]
				modulesDict[collection] = cl
				print (collection, cl, size)
			except:
				break

		json.dump(modulesDict, fileModules, ensure_ascii=False, indent=4 )
