traits = [
'"value": "sol gradient"', #Background
'"value": "base"', #Base
'"value": "lava"', #Fur
'"value": "centurion armor"', #Clothing
'"value": "fire"', #Eye
'"value": "cyborg eye"', #Mouth
'"value": "laser line"', #Eyewear
'"value": "diamond stud"', #Earrings
'"value": "crown"', #Headgear
'"value": "diamond"' #Holding
]

#loop through all traits(_trait) and check if line contains _trait.
def CheckDuplicate(traitline):
    for trait in traits:
        if trait in traitline:
            #print(f"Trait: {trait} "
            #      f"in \n {traitline} ")
            return True

    return False

# GLOBAL VARIABLES
fileIndex = int()
fileSize = 11879
duplicate = 0       #REDUNDANT
duplicateList = []

def main():
    fileIndex = 11400

    # Iterating through all files.
    while(fileIndex <= fileSize):
        f = open(str(fileIndex) + ".json", "r")
        flagCount = 0       # Flag Counter, if 10 then duplicate.

        print(f"Looping file: {str(fileIndex)}.json")       # Debug.

        # Iterating through all lines in file.
        for line in f:
            flag = CheckDuplicate(line)     # Trait Checker.

            if(flag):
                flagCount += 1              # Increment FlagCounts.


        print(f"File: {fileIndex}.json has {flagCount} flags...")       # Debug.

        if(flagCount == 10):            # if duplicate.
            print(f"Duplicate: {fileIndex}.json")
            duplicateList.append(f"{fileIndex}.json")

        f.close()       # close file.
        fileIndex = fileIndex + 1       # Iterate through indexs.

    print(f"Found duplicates: {duplicateList}")     # Output

main()
