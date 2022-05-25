#!/bin/bash

edmEventSize -o eventSize.txt -F /eos/project/c/cmsweb/www/reco-prof/circles/data/CMSSW_12_4_0_pre2/slc7_amd64_gcc10/11834.21/step3.root



python3 jsonDump.py eventSize.txt eventSize.json



#./../circles/scripts/find_unassigned.py eventSize.json



python3 makeGroup.py eventGroup.txt eventsizegroup.json
