import json
import CosineSimilarity as CS

DebugFlag = 0
def DebugSection(s):
    if not DebugFlag:
        return

    print("//////////DEBUG SECTION START")
    print(s)
    print("//////////DEBUG SECTION END")
def ReloadJsonFile(file):
    f = open(file)  # 2
    FAQData = json.load(f)  # 3
    f.close()
    for i in FAQData:
        DebugSection(i+" : "+FAQData[i])
    return FAQData

MinThresholdAcceptable = 0.1
FAQData = ReloadJsonFile('FAQ.json')
AUX = {"Question" : "-","Coefficient" : -1,"Answer" : "-"}
while (True):
    print("Smart System to answer pharmaceutical questions"
          "\nType exit if you wish to leave the program"
          "\nPlease input your questions below:")
    UserInput = input()  # 4
    if UserInput == "exit":
        print("Exiting now...")
        break

    for i in FAQData.keys():
        Coefficient = CS.CosineSimilarityFunction(i, UserInput) # 5
        DebugSection(Coefficient)
        if AUX["Coefficient"] < Coefficient: #6
            AUX["Question"] = i
            AUX["Coefficient"] = Coefficient
            AUX["Answer"] = FAQData[i]

    if AUX["Coefficient"] > MinThresholdAcceptable:
        print(AUX["Answer"]+"...\n\n")
    else:
        print("Unable to find a suitable answer try again\n...\n")