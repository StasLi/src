def sumrec (n):
    if n==0:
        return 0
    else:
        return n+sumrec(n-1)

def minimumelement (array,size):
    if size == 1:
        return array[0]
    else:
        return min(array[0],minimumelement(array[1:],size-1))


def minimumelementfor (array,size):
    minimum = array[0]
    for i in range(size-1):
        if minimum>array[i+1]:
            minimum = array[i+1]
    return minimum

def sumarray (array,sum):
    if len(array)==0:
        return sum
    return sumarray(array[1:],sum+array[0])

def palindrome(inputstring):
    length = len(inputstring)
    for i in range(length//2):
        if inputstring[i]!=inputstring[length-i-1]:
            return False
    return True

def palinddromerec(istring):
    if len(istring) <= 1:
        return True

    if istring[0]==istring[len(istring)-1]:
        return palinddromerec(istring[1:-1])
    else:
        return False


def binarysearch (array,target):
    pointer = ((len(array)))//2
    print(array)
    if len(array)==1 and array[0]!=target:
        return False
    if array[pointer] == target:
        return True
    if target > array[pointer]:
        return binarysearch(array[pointer:],target)

    else:
        return binarysearch(array[:pointer],target)
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

def mergesort(list_a):
    print(list_a)
    if len(list_a) <= 1:
        return list_a

    middle = len(list_a)//2

    list1 = list_a[:middle]
    list2 = list_a[middle:]

    print('list1',end='')
    print(list1)
    print('list2',end='')
    print(list2)
    return combinelists(mergesort(list1),mergesort(list2))












def main():
    #print(sumrec(5))
    #print (minimumelement([1,0,2,5,54],5))
    #print(minimumelementfor([3, 4, 8, 5, 2], 5))
    #print(sumarray([1,5,2,5,5],0))
    #print(palindrome('a'))
    #print(palinddromerec('fxcbcxa'))
    #print(binarysearch([-2,-1,0],23))
    print (mergesort([3, 4, 8, 5,6, 2]))



if __name__ == '__main__':
    main()

