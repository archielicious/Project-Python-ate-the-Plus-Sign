#Program to find the Collatz Sequence of a number and counting the steps
def collatz_seq_indv_prog_one():
    n=input('Enter a number of which you want to find the sequence in the Collatz conjecture')
    N=int(n)
    a=None
    step=0
    result=True
    print('The sequence of',n,'in the Collatz conjecture is')
    print(N)
    while result:
        if N%2==1:
            a=(3*N)+1
            step=step+1
            print(int(a))
            N=a
        else:
            a=N/2
            step=step+1
            print(int(a))
            N=a
            if N!=1:
                continue
            else:
                print('steps=',step)
                result=False
