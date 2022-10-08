import json

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class file:
    def __init__(self, list):
        self.traits = list

filelist = []

def CheckTrait(referencetraits, current_trait):
    for trait in referencetraits:
        if trait == current_trait:
            return True

    return False


def main():
    c = 0
    dlist = []

    for x in range(0, 119):
        f = open("root/" + str(x) + ".json")
        y = json.load(f)

        slist = []
        for x in y["attributes"]:
            slist.append("{}: {}".format(list(x.items())[0][1], list(x.items())[1][1]))

        filelist.append(file(slist))

    for x in range(0, 11879):
        f = open(str(x) + ".json")
        y = json.load(f)

        slist = []
        for q in y["attributes"]:
            slist.append("{}: {}".format(list(q.items())[0][1], list(q.items())[1][1]))

        for z in filelist:
            a = 0

            for w in slist:
                if CheckTrait(z.traits, w):
                    a += 1

            if a == len(slist):
                dlist.append(x)
                #print(f"Duplicate ID: {x}.json")

            c += 1

            if(c%151 == 0):
                #cls()
                print(f"{c} out of {11879*119}")

    if(len(dlist) == 0):
        print("No Duplicates")
    else:
        print("Duplicates:")
        for x in dlist:
            print(f" - {x}.json")

main()
