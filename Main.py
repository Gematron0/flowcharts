import Input_Data
from Input_Data import dayOfInput, reasonOfInput, monthOfInput, yearOfInput, ammouOfMoney, posOrNegEntry
import GUI_Scripts
from GUI_Scripts import clearConsole, resetOptions, inputSystem
import Defalt_Reasons
from Defalt_Reasons import defaltReasonsSelection, creatReasons, creatReasonQuickForm, maxValueSelection, minValueSelection, saveDatoForReasons, removeDatoForReason, settings

import os
import colorama
from colorama import Fore, Back
import time
colorama.init(autoreset=True)

### selection screan selector code to run whitch function
def selectionScreen():
    while True:
        print ("--------------------")
        print ("  SELECT SOMETHING  ")
        print ("(01) add a new entry")
        print ("(02) display information")
        print ("(03) add a defalt reason")
        print ("(04) accses the settings and change them")
        inp = inputSystem(0, 0, 3)
        if inp == "01" or inp == "1":
            return 1
        elif inp == "02" or inp == "2":
            return 2
        elif inp == "03" or inp == "3":
            return 3
        elif inp == "04" or inp == "4":
            return 4
        else:
            resetOptions()

###### VARABLESE #####
DefaltReasonList = []
DefaltQuckReaosonList = []

###### MAIN CODE #####
while True:
    clearConsole()
    selection = selectionScreen()
    print (selection)
    clearConsole()
    while selection == 1:
        posOrNegEntry()
        clearConsole()
        ammouOfMoney()
        clearConsole()
        yearOfInput()
        clearConsole()
        monthOfInput()
        clearConsole()
        dayOfInput()
        clearConsole()
        DefaltReasonList, DefaltQuckReaosonList = reasonOfInput(DefaltReasonList, DefaltQuckReaosonList)
        clearConsole()

    while selection == 3:
        ReasonSelection = defaltReasonsSelection(DefaltReasonList, DefaltQuckReaosonList)
        clearConsole()
        if ReasonSelection == 1:
            CreRaas = creatReasons()
            clearConsole()
            CreRaasFoQui = creatReasonQuickForm()
            clearConsole()
            DefaltReasonList, DefaltQuckReaosonList = saveDatoForReasons(DefaltReasonList, DefaltQuckReaosonList, CreRaas, CreRaasFoQui)
            clearConsole()

        elif ReasonSelection == 2:
            DefaltReasonList, DefaltQuckReaosonList = removeDatoForReason(DefaltReasonList, DefaltQuckReaosonList)
            clearConsole()
            
        elif ReasonSelection == 3:
            selection = 0
        
    while selection == 4:
        section = settings()
        if section == 1:
            clearConsole()
            maxValueSelection()
        elif section == 2:
            clearConsole()
            minValueSelection()

