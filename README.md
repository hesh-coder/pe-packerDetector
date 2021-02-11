# pe-packerDetector

Reads a given PE file and scans sections within it using pefile, comparing the section names within this file to a set of    
known packed section names, with this set of names being generated from a given text file containing known packed section names (provided in this repo). 

This is run with: 
$ ./myPackerDetector.py -target_malware {pathToPE} -known_packers {pathToPackerNames} 
 
As said above, a file of some known packer names is included in this repo.
