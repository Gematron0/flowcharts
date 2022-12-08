import os
import colorama
from colorama import Fore, Back
import time
colorama.init(autoreset=True)#

def staderdiseMonths(WhatMonth):
    if WhatMonth == "1" or WhatMonth == "01" or WhatMonth == "Jan" or WhatMonth == "Janary" or WhatMonth == "jan" or WhatMonth == "janary":
        return("01")
    elif WhatMonth == "2" or WhatMonth == "02" or WhatMonth == "Feb" or WhatMonth == "February" or WhatMonth == "feb" or WhatMonth == "february":
        return("02")
    elif WhatMonth == "3" or WhatMonth == "03" or WhatMonth == "Mar" or WhatMonth == "March" or WhatMonth == "mar" or WhatMonth == "march":
        return("03")
    elif WhatMonth == "4" or WhatMonth == "04" or WhatMonth == "Apr" or WhatMonth == "April" or WhatMonth == "apr" or WhatMonth == "april":
        return("04")
    elif WhatMonth == "5" or WhatMonth == "05" or WhatMonth == "May" or WhatMonth == "May" or WhatMonth == "may" or WhatMonth == "may":
        return("05")   
    elif WhatMonth == "6" or WhatMonth == "06" or WhatMonth == "Jun" or WhatMonth == "June" or WhatMonth == "jun" or WhatMonth == "june":    
        return("06")  
    elif WhatMonth == "7" or WhatMonth == "07" or WhatMonth == "Jul" or WhatMonth == "July" or WhatMonth == "jul" or WhatMonth == "july":
        return("07")
    elif WhatMonth == "8" or WhatMonth == "08" or WhatMonth == "Aug" or WhatMonth == "August" or WhatMonth == "aug" or WhatMonth == "august":
        return("08")
    elif WhatMonth == "9" or WhatMonth == "09" or WhatMonth == "Sep" or WhatMonth == "September" or WhatMonth == "sep" or WhatMonth == "september":
        return("09")
    elif WhatMonth == "10" or WhatMonth == "10" or WhatMonth == "Oct" or WhatMonth == "October" or WhatMonth == "oct" or WhatMonth == "october":
        return("10")
    elif WhatMonth == "11" or WhatMonth == "11" or WhatMonth == "May" or WhatMonth == "November" or WhatMonth == "nov" or WhatMonth == "november":
        return("11")   
    elif WhatMonth == "12" or WhatMonth == "12" or WhatMonth == "Dec" or WhatMonth == "December" or WhatMonth == "dec" or WhatMonth == "december":    
        return("12")
    else:
        return("00")  
    
def checkMonths(WhatMonth):
    if WhatMonth == "1" or WhatMonth == "2" or WhatMonth == "3" or WhatMonth == "4" or WhatMonth == "5" or WhatMonth == "6" or WhatMonth == "7" or WhatMonth == "8" or WhatMonth == "9" or WhatMonth == "10" or WhatMonth == "11":
        return (True)
    elif WhatMonth == "01" or WhatMonth == "02" or WhatMonth == "03" or WhatMonth == "04" or WhatMonth == "05" or WhatMonth == "06" or WhatMonth == "07" or WhatMonth == "08" or WhatMonth == "09":
        return (True)
    elif WhatMonth == "Jan" or WhatMonth == "Feb" or WhatMonth == "Mar" or WhatMonth == "Apr" or WhatMonth == "May" or WhatMonth == "Jun" or WhatMonth == "Jul" or WhatMonth == "Aug" or WhatMonth == "Sep" or WhatMonth == "Oct" or WhatMonth == "Nov" or WhatMonth == "Dec":
        return (True)
    elif WhatMonth == "Janary" or WhatMonth == "February" or WhatMonth == "March" or WhatMonth == "Aprl" or WhatMonth == "May" or WhatMonth == "June" or WhatMonth == "July" or WhatMonth == "August" or WhatMonth == "September" or WhatMonth == "October" or WhatMonth == "November" or WhatMonth == "December":
        return (True)
    elif WhatMonth == "jan" or WhatMonth == "feb" or WhatMonth == "mar" or WhatMonth == "apr" or WhatMonth == "may" or WhatMonth == "jun" or WhatMonth == "jul" or WhatMonth == "aug" or WhatMonth == "sep" or WhatMonth == "oct" or WhatMonth == "nov" or WhatMonth == "dec":
        return (True)
    elif WhatMonth == "janary" or WhatMonth == "february" or WhatMonth == "march" or WhatMonth == "aprl" or WhatMonth == "may" or WhatMonth == "june" or WhatMonth == "july" or WhatMonth == "august" or WhatMonth == "september" or WhatMonth == "october" or WhatMonth == "november" or WhatMonth == "december":
        return (True)
    else:
        return(False)

def minMaxMoney(type, moneyAmmount):
    if type == 1:
        MinValueMoney = moneyAmmount
    if type == 2:
        MaxValueMoney = moneyAmmount
    if type == 3:
        if MinValueMoney >= moneyAmmount and MaxValueMoney <= moneyAmmount:
            return(True)
        else:
            return(False)

### looks at the month people have inputed and the ammount of dayes there is inside the input ###
def checkDay(WhatDay, WhatMonth):
    if WhatMonth == "01":
        if WhatDay >= 0 and WhatDay <= 31:
            return(True)
        else:
            return(False)
    
    if WhatMonth == "02":
        if WhatDay >= 0 and WhatDay <= 28:
            return(True)
        else:
            return(False)

    if WhatMonth == "03":
        if WhatDay >= 0 and WhatDay <= 31:
            return(True)
        else:
            return(False)

    if WhatMonth == "04":
        if WhatDay >= 0 and WhatDay <= 30:
            return(True)
        else:
            return(False)
    
    if WhatMonth == "05":
        if WhatDay >= 0 and WhatDay <= "31":
            return(True)
        else:
            return(False)

    if WhatMonth == "06":
        if WhatDay >= 0 and WhatDay <= "30":
            return(True)
        else:
            return(False)

    if WhatMonth == "07":
        if WhatDay >= 0 and WhatDay <= "31":
            return(True)
        else:
            return(False)
            
    if WhatMonth == "08":
        if WhatDay >= 0 and WhatDay <= "31":
            return(True)
        else:
            return(False)

    if WhatMonth == "09":
        if WhatDay >= 0 and WhatDay <= "30":
            return(True)
        else:
            return(False)

    if WhatMonth == "10":
        if WhatDay >= 0 and WhatDay <= "31":
            return(True)
        else:
            return(False)

    if WhatMonth == "11":
        if WhatDay >= 0 and WhatDay <= "30":
            return(True)
        else:
            return(False)

    if WhatMonth == "12":
        if WhatDay >= 0 and WhatDay <= "31":
            return(True)
        else:
            return(False)