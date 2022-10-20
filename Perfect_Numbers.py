#Program to find the perfect numbers starting from 2
def perfect_number():
    n=input('Enter the number upto which you want to find the perfect numbers')
    N=int(n)
    index=0
    for i in range(2,N+1):
        value=0
        print('Divisors of',i,'are')
        for a in range(1,(i//2)+1):
            if i%a==0:
                print(a)
                value=value+a
        print('Total of divisors of',i,'=',value)
        if value==i:
            print(i,'is a perfect number')
            index=index+1
        else:
            print(i,'is not a perfect number')
    print('Number of total perfect numbers upto',N,'is',index)
