#Program to find the cumulative sum of a list of numbers
def cumulative_sum():
    N=input('Enter the number of entries in the list')
    lst=list()
    n_lst=list()
    for i in range(0,int(N)):
        a=input('Enter a number')
        if a=='Done':
            break
        else:
            b=int(a)
            lst.append(b)
    print('The original list is',lst)
    n_lst.append(lst[0])
    for i in range(1,len(lst)):
        n_lst.append(n_lst[i-1]+lst[i])
    print('The list having the cumulative sum of the original list is',n_lst)
