from datetime import datetime
time = datetime.now()
date = time.strftime("%x")
cTime = time.strftime("%X")
normalAl = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','1','2','3','4','5','6','7','8','9','0','\t','\n']
codingAl = ['E','J','O','T','Y','X','S','N','I','D','C','H','M','R','W','V','Q','L','G','B','0','F','K','P','U','A','Z','*','$',')','-','+','%','=','@','<','?',' ','\n']


def mainHeading(): #main headings
    print("✄╭━━━╮╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╭━━━━╮╱╱╱╱╭╮")
    print("✄┃╭━╮┃╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃")
    print("✄┃╰━━┳━━┳╮╭╮╭┫╰━━┳━━┳━╋╯┃┃┣┻━┳━━┫╰━╮")
    print("✄╰━━╮┃╭╮┃╰╯╰╯┣━━╮┃╭╮┃╭╮╮┃┃┃┃━┫╭━┫╭╮┃")
    print("✄┃╰━╯┃╭╮┣╮╭╮╭┫╰━╯┃╭╮┃┃┃┃┃┃┃┃━┫╰━┫┃┃┃")
    print("✄╰━━━┻╯╰╯╰╯╰╯╰━━━┻╯╰┻╯╰╯╰╯╰━━┻━━┻╯╰╯")
    print("-------------------------------------------------------------------------------")
    print("welcome to Sawsan's Code Words bV_2.1.0 (beta version)")
    
def secondaryMeny():
    print("-------------------------------------------------------------------------------")
    print("1.Encoding (From simple sentence to code sentence.\n2.Decoding (from code sentence to simple sentence.")
    print("Exit/EXIT/exit(Any one word): To Shut Down ")
    print("Please select 1 or 2 or Exit")

def encodingFunction(ePromt): #encoding func
    userPromtListA = []
    resultListA = []
    encodingF = ePromt
    for letter in encodingF:
        userPromtListA.append(letter)
    for i in range(0, len(userPromtListA)):
        index = normalAl.index(userPromtListA[i])
        resultListA.append(codingAl[index])
    print("Decoded text: "+"".join(userPromtListA))
    print("Encoded text: "+"".join(resultListA))

def decodingFunction(dPromt):  #decoding func
    userPromtListB = []
    resultListB = []
    decodingF = dPromt
    for letter in decodingF:
        userPromtListB.append(letter)
    for i in range(0,len(userPromtListB)):
        index = codingAl.index(userPromtListB[i])
        resultListB.append(normalAl[index])
    print ("Encoded text: "+"".join(userPromtListB))
    print("Decoded text: "+"".join(resultListB))

mainHeading()

while(True):
    secondaryMeny()
    userPromt = str(input("Type here: "))
    if(userPromt == "1"):
        encodePromt = str(input("Type your SIMPLE sentence here: "))
        newUserA = encodePromt.upper()
        encodingFunction(newUserA)
        continue
    elif(userPromt == "2"):
        decodePromt = str(input("Type your ENCODED sentence here: "))
        newUserB = decodePromt.upper()
        decodingFunction(newUserB)
        continue
    elif(userPromt=="EXIT" or userPromt=="exit" or userPromt=="Exit"):
        print("Thank you")
        print("Procces Finished\n")
        print("Created on October 08, 2021\nWritten By: Sawsan Niom\nCurrent Time:\n{}\n{}".format(date, cTime))
        break
    else:
        print("Wrong Input, Try Again")
        mainHeading()
        continue




