#Program to find the lcm of a number of numbers
def lcm():
    n=input('Enter the number of numbers of which you want to find the lcm or least common multiple')
    a=int(n)
    lst=list()
    for i in range(1,a+1):
        b=input('Enter a Number')
        if b=='Done':
            break
        else:
            c=int(b)
            lst.append(c)
    print('The list of the numbers is',lst)
    largest=None
    for i in lst:
        if largest==None:
            largest=i
        elif i>largest:
            largest=i
    print('The largest number in the list is',largest)
    N=2
    k=largest 
    j=k
    result=True
    while result:
        for x in lst:
            if j%x==0:
                if not x==lst[-1]:
                    continue
                print('The lcm of the list of the numbers is',j)
                result=False
            else:
                j=N*k
                N=N+1
                x=lst[0]
                break
