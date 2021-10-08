from datetime import datetime
time = datetime.now()
date = time.strftime("%x")
cTime = time.strftime("%X")
userPromtList = []
resultList = []
normalAl = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','\n']
codingAl = ['E','J','O','T','Y','X','S','N','I','D','C','H','M','R','W','V','Q','L','G','B','0','F','K','P','U','A','Z','\n']


def mainHeading(): #main headings
    print("@@@@@@@@      @@    @@       @       @@  @@@@@@@@       @@       @@ @@       @@")
    print("@@          @@  @@  @@      @ @      @@  @@           @@  @@     @@  @@      @@")
    print("@@          @@  @@   @@     @ @     @@   @@           @@  @@     @@   @@     @@")
    print("@@@@@@@@   @@@@@@@@   @@   @@  @@   @@   @@@@@@@@    @@@@@@@@    @@    @@    @@")
    print("      @@   @@    @@   @@   @@  @@  @@          @@    @@    @@    @@     @@   @@")
    print("      @@  @@      @@   @@ @@    @@ @@          @@   @@      @@   @@      @@  @@")
    print("@@@@@@@@ @@        @@   @@       @@      @@@@@@@@  @@        @@  @@       @@ @@")
    print("-------------------------------------------------------------------------------")
    print("welcome to Sawsan's Code Words bV_1.1.2 (beta version)")
    print("only use BLOCK/CAPITAL LETTER please")
    print("-------------------------------------------------------------------------------")
    print("1.Encoding (From simple sentence to code sentence.\n2.Decoding (from code sentence to simple sentence.")
    print("Please select 1 or 2")

def getInput(): #input func
    userPromt = str(input("Type here: "))
    return userPromt

def encodingFunction(): #encoding func
    encodingF = open("SimpleText.txt")
    for letter in encodingF.read():
        userPromtList.append(letter)
    for i in range(0, len(userPromtList)):
        index = normalAl.index(userPromtList[i])
        resultList.append(codingAl[index])
    print("Decoded text: "+"".join(userPromtList))
    print("Encoded text: "+"".join(resultList))

def decodingFunction():  #decoding func
    decodingF = open("CrazzZZzzyText.txt")
    for letter in decodingF.read():
        userPromtList.append(letter)
    for i in range(0,len(userPromtList)):
        index = codingAl.index(userPromtList[i])
        resultList.append(normalAl[index])
    print ("Encoded text: "+"".join(userPromtList))
    print("Decoded text: "+"".join(resultList))

mainHeading()

if(getInput() == "1"):
    encodingFunction()
else:
    decodingFunction()



print("Procces Finished\n")
print("Created on October 08, 2021\nCreated By: Sawsan Niom\nCurrent Time:\n{}\n{}".format(date,cTime))
