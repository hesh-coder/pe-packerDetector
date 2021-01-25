import prefile

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
