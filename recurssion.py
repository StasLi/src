def factorial (a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)

def fibor1(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    fib1=fibor1(num-1)
    fib2=fibor1(num-2)
    return fib1+fib2

#def fibor(num):

    #if num>1:
        #fib1=fibor(num-1)
        #fib2=fibor(num-2)

        #return fib1

print(factorial(6))
print(fibor1(10))


if __name__ == "__main__":
    main()