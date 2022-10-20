#Program to convert a number from any base from base 2 to 9 to its decimal equivalent using doubling method
def any_base_to_decimal_doubling():
    m=input('Enter the base from 2 to 9 in which the number is in')
    n=input('Enter the number you want to convert to decimal')
    M=int(m)
    a=(0*M)+int(n[0])
    for i in range(1,len(n)):
        b=(a*M)+int(n[i])
        a=b
    print('The decimal equivalent of of the number',n,'is',a)
