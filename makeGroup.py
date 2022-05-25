import os
import json
#import string

def main(filename, output):
	fileModules = open(output,"w")
	group = {}
	with open(filename) as f:
		## lineloop
		for l in f:
			l = l.replace("\n","")
			## avoiding lastline
			try:		
				vl = l.split("|")
				print(vl[0])
				disc = vl[0]
				## Mainline clusters
				if 'recoGen' in disc:
					group[l] = "GEN"
				elif 'l1t' in disc:
					group[l] = "L1T"
				elif 'recoPF' in disc:
					group[l] = "Particle Flow"

				else:
					continue
			except:
				break
		print(group)
		json.dump(group,fileModules, ensure_ascii=False, indent=4 )
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



#
