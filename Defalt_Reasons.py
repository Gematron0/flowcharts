from GUI_Scripts import inputSystem, resetOptions, clearConsole

import os
import colorama
from colorama import Fore, Back
import time
colorama.init(autoreset=True)


### letting the players add depalt reasons so they dont have to type the same reason every time ###
def defaltReasonsSelection(DefaltReasonList, DefaltQuckReaosonList):
    inputSystem(1, 3, 1)
    z = 0
    print(Fore.GREEN+"===================================")
    print ("press (01 or 1) to add a defalt reaons onto the list")
    print ("press (02 or 2) to remove a defalt varable name")
    print ("press (03 or 3) to save and return back to the main screen")
    print ("your defalt reason are:")
    for i in DefaltReasonList:
        x = DefaltQuckReaosonList[z]
        z = z + 1
        print ("Short form: (",x,") long form: (",i,") ")
    if z == 0:
        print(Fore.BLACK+Back.YELLOW+"you have none")
    print(Fore.GREEN+"===================================")
    inputSystem(1, 3, 2)
    inp = inputSystem(0, 0, 3)
    if inp == "1" or inp == "01":
        return(1)
    elif inp == "2" or inp == "02":
        return(2)
    elif inp == "3" or inp == "03":
        return(3)
    else:
        resetOptions()
    
### creat reasons ###
def creatReasons():
    inputSystem(2, 2, 1)
    print(Fore.GREEN+"===================================")
    print("input your defalt varable name")
    print(Fore.GREEN+"===================================")
    inputSystem(2, 2, 2)
    inp = inputSystem(0, 0, 3)
    return inp

### cear a quickform for the varables ###
def creatReasonQuickForm():
    inputSystem(3, 1, 1)
    print(Fore.GREEN+"===================================")
    print("creat a quick way for typing the methid(like 01, 1 or staffsallery")
    print(Fore.GREEN+"===================================")
    inputSystem(3, 1, 2)
    inp = inputSystem(0, 0, 3)
    return inp

### saves the data for the quick form varambles ###
def saveDatoForReasons(DefaltReasonList, DefaltQuckReaosonList, CreRaas, CreRaasFoQui):
    print(Fore.BLACK+Back.YELLOW+"SAVING DATA...")
    print(Fore.BLACK+Back.YELLOW+"DO NOT TURN OF THE MECHEN AS THIS CAN LEAD TO CURRUPTION")
    DefaltReasonList.append(CreRaas)
    DefaltQuckReaosonList.append(CreRaasFoQui)
    return DefaltReasonList, DefaltQuckReaosonList

### removes data form a list ###
def removeDatoForReason(DefaltReasonList, DefaltQuckReaosonList):
    z = 0
    inputSystem(2, 2, 1)
    print(Fore.GREEN+"===================================")
    print("wright the short or long form of the data you wish to remove from the list")
    for i in DefaltReasonList:
        x = DefaltQuckReaosonList[z]
        z = z + 1
        print ("Short form: (",x,") long form: (",i,") ")
    if z == 0:
        print(Fore.BLACK+Back.YELLOW+"you have none")
    print(Fore.GREEN+"===================================")
    inputSystem(2, 2, 2)
    inp = inputSystem(0, 0, 3)
    clearConsole()
    print("Checking data")

    q = -1
    for i in DefaltReasonList:
        q = q + 1
        if inp == i:
            clearConsole()
            inputSystem(3, 1, 1)
            x = DefaltQuckReaosonList[q]
            print(Fore.RED+"===================================")
            print("are you shure you wish to delete in Short form: (",x,") long form: (",i,")")
            print("Press (Y) for yes and (n) for no")
            print(Fore.RED+"===================================")
            inputSystem(3, 1, 2)
            int = inputSystem(0, 0, 3)
            if int == "Y":
                DefaltReasonList.pop(q)
                DefaltQuckReaosonList.pop(q)
                return (DefaltReasonList, DefaltQuckReaosonList)

    print(Fore.BLACK+Back.YELLOW+"havent found in 1/2 serched")
    q = -1
    for i in DefaltQuckReaosonList:
        q = q + 1
        if inp == i:
            clearConsole()
            inputSystem(3, 1, 1)
            x = DefaltReasonList[q]
            print(Fore.RED+"===================================")
            print("are you shure you wish to delete in Short form: (",i,") long form: (",x,")")
            print("Press (Y) for yes and (n) for no")
            print(Fore.RED+"===================================")
            inputSystem(3, 1, 2)
            int = inputSystem(0, 0, 3)
            if int == "Y":
                DefaltReasonList.pop(q)
                DefaltQuckReaosonList.pop(q)
                return (DefaltReasonList, DefaltQuckReaosonList)
    resetOptions()
    return (DefaltReasonList, DefaltQuckReaosonList)
    