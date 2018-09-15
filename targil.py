import math
from typing import List


def exercise1():
    Num = input("enter the number")
    Num = int(Num)
    operation = input("choose between sum and factorial[1-2]")
    sum = 0
    operation = int(operation)
    if operation == 2:
        print ("factorial of ", Num," = ",math.factorial(Num))
    elif operation == 1:
       for i in range(0,Num+1):
            sum += i
       print("The sum of numbers is = ", sum)
    else:
        print ("wrong choice")

def exercise2(inputlist):
    length = len(inputlist)

    for i in range(length//2):
        var1 = inputlist[i]
        inputlist[i] = inputlist[length-1-i]
        inputlist[length-i-1]=var1
    return inputlist

def exercise3(inputstring):
    length = len(inputstring)
    for i in range(length//2):
        if inputstring[i]!=inputstring[length-i-1]:
            return False
    return True

def exercise4(list1,list2):
    list3 = list()
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
    return list3


def combinelists(list1,list2):
    length1 = len(list1)
    length2 = len(list2)
    list3=list()
    pos_a=0
    pos_b=0

    while len(list3)<(length1+length2):
        if pos_a < length1 and pos_b < length2:
            if list1[pos_a]<list2[pos_b]:
                list3.append(list1[pos_a])
                pos_a += 1
            else:
                list3.append(list2[pos_b])
                pos_b += 1
        elif pos_a < length1:
            list3.append(list1[pos_a])
            pos_a+=1
        elif pos_b<length2:
            list3.append(list2[pos_b])
            pos_b+=1

    return(list3)


def fibo():
    var1 = 1
    var2 = 1
    print("1 1 ",end="")
    for i in range(2,10):
        f = var1 + var2
        print(f," ",end="")
        var2=var1
        var1=f



def exercise6(inputlist):
    width = len(max(inputlist, key=len))+3
    height = len(inputlist)
    counter: List[int] = list()
    for i in range(width):
        print ("*", end="")
    print("*")
    #upper line printed
    for i in range(height):
       counter.append(len(inputlist[i]))
    #list of strings length

    for i in range (height):
        print("*",end = "")
        innercounter = (width - counter[i])//2
        for j in range(innercounter):
            print(" ",end="")
        #print(" ")
        print(inputlist[i],end="")
        if width%2 != 0:
            if int(counter[i])% 2 == 0:
                innercounter = (width - counter[i]) // 2
                for j in range(innercounter):
                    print(" ",end="")
            else:
                innercounter = (width - counter[i]) // 2-1
                for j in range(innercounter):
                    print(" ", end="")
        if width%2 == 0:
            if int(counter[i])% 2 == 0:
                innercounter = (width - counter[i]) // 2-1
                for j in range(innercounter):
                    print(" ",end="")
            else:
                innercounter = (width - counter[i]) // 2
                for j in range(innercounter):
                    print(" ", end="")

        print("*")
    






    for i in range(width+1):
        print ("*", end="")


    return ("")







def main():
    #exercise1()
    #print(exercise2([1,2]))
    #print(exercise3("abcxa"))
     #print(combinelists([8,3,7],[4,5,30]))
    print(exercise6(["awhyddk", "zzz", "b","aa","hello"]))
    #print(exercise4(["ab","bc","de"],[1,2,3]))
    #fibo()



if __name__ == "__main__":
    main()



