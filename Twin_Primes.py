#Program to find the twin prime pairs upto a number
def twin_primes():
    n=input('Enter the number upto which you want to find the twin primes')
    N=int(n)
    lst=list()
    if n=='2' or n=='3':
        print('There are no twin primes upto',N)
    else:
        for i in range(2,N-2+1):
            for x in range(2,((i//2)+1)):
                if i%x==0:
                    break
            else:
                p=i+2
                for q in range(2,((p//2)+1)):
                    if p%q==0:
                        break
                else:
                    lst.append((i,p))
        if len(lst)==0:
            print('There are no twin primes upto',N)
        else:
            print('The number of pairs of twin primes upto',N,'is',len(lst))
            print('The twin prime pairs upto',N,'are')
            print (*lst,sep=', ')
