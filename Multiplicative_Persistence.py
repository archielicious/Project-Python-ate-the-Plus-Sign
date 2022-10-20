#Program to find the Multiplicative Persistence of a number
def multi_persi():
    n=input('Enter a number')
    product=1
    steps=0
    result=1
    print('The products are')
    if len(n)!=1:
        for i in range(0,len(n)):
            product=product*int(n[i])
        print(product)
        steps=steps+1
        while len(str(product))!=1:
            a=str(product)
            for x in range(0,len(a)):
                product=result*int(a[x])
                result=product
            print(product)
            result=1
            steps=steps+1
        print('steps=',steps)
    else:
        print(int(n))
        print('steps=',0)
