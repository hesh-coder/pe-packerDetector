import pefile

def importKnownPackers(filePath):
    knownPackers = set()
    try:
        with open(filePath) as packerPath:
            for line in packerPath:
                knownPackers.add(line.strip)
    except:
        print("Error reading given file.")
        return None

    return knownPackers

def detectPackers(pe, knownPackers):
    foundPackers = set()
    for section in pe.sections:
        if section.name in knownPackers:
            matches.add(section.name)

    return foundPackers

if __name__ = '__main__':
	parser = argparse.ArgumentParser(
		description="Identify packers in a given file"
	)

	parser.add_argument(
		"-target_malware",
		help="Target file for packet analysis."
	)	
			
	parser.add_argument(
		"-known_packers",
		help="File of known packers to import."
	)
	
	args = parser.parse_args()
	targetFile = args.target_file
	knownPackerFile = args.known_packers

	knownPackers = importKnownPackers(knownPackerFile)
	detectedPackers = detectPackers(targetFile, knownPackers)

	print("Packers detected in ", targetFile, " :")
	for item in detectedPackers:
		print(item)		
