#Program to find the factorial of a number
def factorial_indv():
    n=input('Enter the number of which you want to find the factorial')
    i=int(n)
    value=i
    if int(n)<0:
        print('Factorial domain is defined for positive whole numbers only')
    elif int(n)==1:
        print('The factorial of the number',1,'is',1)
    elif int(n)==0:
        print('The factorial of the number',0,'is',1)
    else:
        while i>0:
            value=value*(i-1)
            i=i-1
            if i==1:
                break
        print('The factorial of the number',int(n),'is',value)
