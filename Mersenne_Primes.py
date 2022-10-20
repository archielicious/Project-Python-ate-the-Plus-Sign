#program to find the mersenne primes upto a number
def mersenne_primes():
    n=input('Enter a number upto which you want to find the mersenne prime')
    N=int(n)
    index=0
    i=2
    while (2**i)<=N+1:
        a=(2**i)-1
        for x in range(2,((a//2)+1)):
            if a%x==0:
                print(a,'equals',x,'*',a//x)
                print(a,'is not a mersenne prime')
                i=i+1
                break
        else:
            print(a,'is a mersenne prime')
            index=index+1
            i=i+1
    print('The number of mersenne prime upto',N,'is',index)
