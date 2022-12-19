from CheckData import checkDay, checkMonths,  minMaxMoney, staderdiseMonths, checkYear
from GUI_Scripts import inputSystem, resetOptions, clearConsole
from Defalt_Reasons import creatReasons,creatReasonQuickForm, saveDatoForReasons

import os
import colorama
from colorama import Fore, Back
import time
colorama.init(autoreset=True)

### sotrs the valus saved in the other programs ###
def storredValues(selector,value):
    if selector == 1:
        UpOrDown = value
        return
    
    if selector == 2:
        moneyAmmount = value
        return

    if selector == 3:
        WhatYear = value
        return

    if selector == 4:
        WhatMonth = value
        return

    if selector == 5:
        WhatDay = value
        return

    if selector == 6:
        ReasonForInput = value
        return
        
    if selector == 7:
        return(UpOrDown, moneyAmmount, WhatDay, WhatMonth, WhatYear, ReasonForInput)

### asks the used if its an + or - entry ###
def posOrNegEntry():
    while True:
        inputSystem(1, 8, 1)
        print(Fore.GREEN+"===================================")
        print ("was the money a positive or negitive ammount")
        print ("select (+ or 01 or 1 or Y) if + entry")
        print ("select (- or 02 or 2 or N) if - entry")
        print(Fore.GREEN+"===================================")
        inputSystem(1, 8, 2)
        inp = inputSystem(0, 0, 3)
        if inp == "01" or inp == "1" or inp == "+" or inp == "Y":
            storredValues (1,"+")
            return
        elif inp == "02" or inp == "2" or inp == "-" or inp == "N":
            storredValues (1,"-")
            return
        else:
            resetOptions()

### akes the user the ammout of money ###
def ammouOfMoney():
    while True:
        inputSystem(2, 7, 1)
        print(Fore.GREEN+"===================================")
        print ("type in the ammout of money")
        print(Fore.GREEN+"===================================")
        inputSystem(2, 7, 2)
        inp = inputSystem(0, 0, 3)
        storredValues (2, inp)
        return

### asks what year the muney was added in ###
def yearOfInput():
    while True:
        inputSystem(3, 6, 1)
        print(Fore.GREEN+"===================================")
        print ("type what year the money was inputed")
        print(Fore.GREEN+"===================================")
        inputSystem(3, 6, 2)
        inp = inputSystem(0, 0, 3)
        storredValues (3, inp)
        return

### asks what month the muney was added in ###
def monthOfInput():
    while True:
        inputSystem(4, 5, 1)
        print(Fore.GREEN+"===================================")
        print ("type what month the money was inputed")
        print(Fore.GREEN+"===================================")
        inputSystem(4, 5, 2)
        inp = inputSystem(0, 0, 3)
        storredValues (4, inp)
        return

### asks what day the muney was added in ###
def dayOfInput():
    while True:
        inputSystem(5, 4, 1)
        print(Fore.GREEN+"===================================")
        print ("type what day the money was inputed")
        print(Fore.GREEN+"===================================")
        inputSystem(5, 4, 2)
        inp = inputSystem(0, 0, 3)
        storredValues (5, inp)
        return

### asks what reason it was input for ###
def reasonOfInput(DefaltReasonList, DefaltQuckReaosonList):
    while True:
        z = 0
        inputSystem(6, 3, 1)
        print(Fore.GREEN+"===================================")
        print ("type what/ how did you get this money from")
        for i in DefaltReasonList:
            x = DefaltQuckReaosonList[z]
            z = z + 1
            print ("Short form: (",x,") long form: (",i,") ")
        if z == 0:
            print(Fore.BLACK+Back.YELLOW+"you have none")
        print(Fore.GREEN+"===================================")
        inputSystem(6, 3, 2)
        inp = inputSystem(0, 0, 3)

        q = -1
        for i in DefaltReasonList:
            q = q + 1
            if inp == i:
                clearConsole()
                x = DefaltQuckReaosonList[q]
                storredValues (6, inp)
                return(DefaltReasonList, DefaltQuckReaosonList)

        q = -1        
        for i in DefaltQuckReaosonList:
            q = q + 1
            if inp == i:
                clearConsole()
                x = DefaltReasonList[q]
                storredValues (6, inp)
                return(DefaltReasonList, DefaltQuckReaosonList)

        if z == 0:
            clearConsole()
            print("This data value dosnet exsist, I will be sending you to make a data type section of this code in 3 seconds")
            time.sleep(3)
            clearConsole()
            CreRaas = creatReasons()
            clearConsole()
            CreRaasFoQui = creatReasonQuickForm()
            clearConsole()
            DefaltReasonList, DefaltQuckReaosonList = saveDatoForReasons(DefaltReasonList, DefaltQuckReaosonList, CreRaas, CreRaasFoQui)
            clearConsole()
        else:
            clearConsole()
            print("your varable:",inp,"dosent exsist,do you wish to creat a new one or retype the data")
            inputSystem(1, 1, 1)
            print(Fore.GREEN+"===================================")
            print ("do you wish to creat a new defalt varable (Y, n)")
            print(Fore.GREEN+"===================================")
            inputSystem(1, 1, 2)
            inp = inputSystem(0, 0, 3)
            if inp == "Y":
                clearConsole()
                CreRaas = creatReasons()
                clearConsole()
                CreRaasFoQui = creatReasonQuickForm()
                clearConsole()
                DefaltReasonList, DefaltQuckReaosonList = saveDatoForReasons(DefaltReasonList, DefaltQuckReaosonList, CreRaas, CreRaasFoQui)
                clearConsole()
            else:
                resetOptions()

### starts to check if any of the data imputed is wrong or not allowed ###
def checkingData():
    moneyAmmountCheck = False
    WhatMonthCheck = False
    WhatDayCheck = False
    clearConsole()
    inputSystem(7, 2, 1)
    print(Fore.GREEN+"===================================")
    print("checking that imputed data for flaws")
    print(Fore.GREEN+"===================================")
    inputSystem(7, 2, 2)
    UpOrDown, moneyAmmount, WhatDay, WhatMonth, WhatYear, ReasonForInput = storredValues(7)
    print("checking for pos and neg entry")

    moneyAmmountCheck = minMaxMoney(3, moneyAmmount)
    
    WhatMonth = staderdiseMonths(WhatMonth)
    WhatMonthCheck = checkMonths(WhatMonth)
    WhatDayCheck = checkDay(WhatDay, WhatMonth)
    checkYear(3, WhatYear)

    if WhatDayCheck == False:
        print(">> Invalid Day inputed")

    if WhatMonth == "00":
        print(">> Invalid Month inputed")

    if moneyAmmountCheck == False:
        print(">> Invalid Month inputed")
