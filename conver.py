#-------------------------------------------------------------------------------
# Name:        convert
# Purpose:
#
# Author:      mejonzhan
#
# Created:     01/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
# decimal convert any base like binary, oct, hex, etc.
#-------------------------------------------------------------------------------
import sys
def main():
    decimal = eval(input("please input the decimal for converting binary: "))
    base = eval(input("please input base: "))
    decimalToNBaseByNormal(decimal, base)
    decToNBaseByRecursion(decimal, base)

def decimalToNBaseByNormal(decimalVar, base):
    tempList = []
    temp = decimalVar
    i = 0
    while (temp > 0):
        ord = temp % base
        if (ord > 9):
            ord = chr(65 + (ord - 10))
        tempList.append(ord)
        temp = int(temp / base)
        i = i + 1
    tempList.reverse();
    #print(tempList)
    binary = ""
    for j in range(len(tempList)):
        binary = binary + str(tempList[j]);
    print("the decimal is: %d and after convering by %d base is %s"%(decimalVar, base, binary))

def decToNBaseByRecursion(dec, base):
    if (dec == 0):
        return
    decToNBaseByRecursion(int(dec/base), base)
    ord = dec % base
    if (ord > 9):
        ord = chr(65 + (ord - 10))
    sys.stdout.write(str(ord))

if __name__ == '__main__':
    main()