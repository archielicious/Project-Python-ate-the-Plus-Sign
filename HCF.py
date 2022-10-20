#Program to find the hcf of a number of numbers
def hcf_prog_two():
    n=input('Enter the number of numbers of which you want to find the hcf or highest common factor')
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
    smallest=None
    for i in lst:
        if smallest==None:
            smallest=i
        elif i<smallest:
            smallest=i
    print('The smallest number in the list is',smallest)
    k=smallest
    lt=list()
    for j in range(k,0,-1):
        if k%j==0:
            lt.append(j)
    y=1
    result=True
    while result:
        for x in lst:
            if x%k==0:
                if not x==lst[-1]:
                    continue
                print('The hcf of the list of the numbers is',k)
                result=False
            else:
                while y<len(lt):
                    k=lt[y]
                    break
                y=y+1
                x=lst[0]
                break
