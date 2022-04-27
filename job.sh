#!/bin/bash

edmEventSize -o Eventsize.txt /eos/project/c/cmsweb/www/reco-prof/circles/data/CMSSW_12_4_0_pre2/slc7_amd64_gcc10/11834.21/step3.root
python3 jsonDump.py Eventsize.txt
