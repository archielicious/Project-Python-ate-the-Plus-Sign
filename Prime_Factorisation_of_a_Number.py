#Program to find the prime factorisation of a number
def prime_factorisation_indv_prog_one():
    n=input('Enter a number of which you want to find the prime factors')
    N=int(n)
    print('The prime factorisation of the number') 
    for a in range(2,(N//2)+1):
        if N%a==0:
            lst=list()
            result=True
            while result:
                p=N
                for i in range(2,int(p//2)+1):
                    if p%i==0:
                        break
                lst.append(i)
                N=N/i
                i=2
                if N!=2:
                    for x in range(2,((int(N)//2)+1)):
                        if int(N)%x==0:
                            result=True
                            break
                    else:
                        result=False
                        if N!=1:
                            lst.append(int(N))
                        else:
                            result=False
                            break
                else:
                    result=True
            print(int(n),'=',end=' ') 
            print(*lst,sep=' × ')
            break
    else:
        print(int(n),'=',1,'×',N)
