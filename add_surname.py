# Author: Mahtab Zilaie
# Date: November 6 2019
# Description: Function using list comprehension names that only start with
# k add surname Kardashian to name

def add_surname(first_names):
    full_list = [i + ' Kardashian' for i in first_names if i[0]=="K"]
    return full_list