#Program to find the Fibonacci Sequence starting from 1 to a given position and find the Fibonacci Number at any position upto this given position
def fibonacci_seq_from_one():
    n=input('Enter the position upto which you want to find the fibonacci sequence')
    N=int(n)
    b=input('Enter the position of the fibonacci number you want to find')
    B=int(b)
    if N==1:
        print('The fibonacci sequence upto the first position starting from',1,'is')
    elif N==2:
        print('The fibonacci sequence upto the second position starting from',1,'is')
    elif N==3:
        print('The fibonacci sequence upto the third position starting from',1,'is')
    else:
        print('The fibonacci sequence upto the',N,'th position starting from',1,'is')
    lst=[1,2,3]
    if N<=3:
       print(lst[0:N])
       if B==1:
           print('First number of the fibonacci sequence is',lst[0])
       elif B==2:
           print('Second number of the fibonacci sequence is',lst[1])
       elif B==3:
           print('Third number of the fibonacci sequence is',lst[2])
    else:
        for i in range(4,N+1):
            lst.append(lst[-1]+lst[-2])
        print(lst)
        if B==1:
            print('First number of the fibonacci sequence is',lst[0])
        elif B==2:
            print('Second number of the fibonacci sequence is',lst[1])
        elif B==3:
            print('Third number of the fibonacci sequence is',lst[2])
        else:
            print(B,'th number of fibonacci sequence is',lst[B-1])
