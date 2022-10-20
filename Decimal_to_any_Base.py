#Program to convert a decimal number to any base equivalent from base 2 to 9
def decimal_to_any_base():
    n=input('Enter the decimal number you want to convert to any base from 2 to 9')
    m=input('Enter the base you want to convert the number to')
    M=int(m)
    N=int(n)
    result=True
    lst=list()
    while result:
        q=N//M
        r=N%M
        lst.append(r)
        N=q
        if q==0:
            result=False
            print('The remainders are',lst)
            lst.reverse()
            print('The decimal number ',n,' when converted to base ',m,' is ',*lst,sep='')
