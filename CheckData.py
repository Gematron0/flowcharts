import os
import colorama
from colorama import Fore, Back
import time
colorama.init(autoreset=True)

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
