#Program to convert a number in any base from base 2 to 9 to its decimal equivalent using positional notation method
def any_base_to_decimal_posn_notn():
    m=input('Enter the base from 2 to 9 in which the number is in')
    n=input('Enter the number you want to convert to decimal')
    M=int(m)
    d=0
    for i in range(0,len(n)):
        a=(M**(len(n)-(i+1)))*int(n[i])
        d=d+a
    print('The decimal equivalent of',n,'is',d)
