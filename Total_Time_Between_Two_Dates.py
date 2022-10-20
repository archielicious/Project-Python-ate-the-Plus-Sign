#Program to find the time between two dates
def time_between_two_dates():
    months={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    yyyymmdd2=input('Enter the date upto which you want to find the total time')
    yyyymmdd1=input('Enter the date from which you want to find the total time')
    dd2=int(yyyymmdd2[7:9])
    dd1=int(yyyymmdd1[7:9])
    yyyy2=int(yyyymmdd2[0:4])
    yyyy1=int(yyyymmdd1[0:4])
    mm2=months[yyyymmdd2[4:7]]
    mm1=months[yyyymmdd1[4:7]]
    if yyyy1>yyyy2 or (yyyy1==yyyy2 and mm1>mm2) or (yyyy1==yyyy2 and mm1==mm2 and dd1>dd2):
        print('The total time can not be found, please enter the date correctly')
    elif (yyyy2%4==0 and yyyy2%100!=0 and mm2==months['Feb'] and dd2>29) or (yyyy2%4==0 and yyyy2%100==0 and yyyy2%400==0 and mm2==months['Feb'] and dd2>29):
        print('Feb in the year',yyyy2,'can not have more than 29 days')
    elif (yyyy1%4==0 and yyyy1%100!=0 and mm1==months['Feb'] and dd1>29) or (yyyy1%4==0 and yyyy1%100==0 and yyyy1%400==0 and mm1==months['Feb'] and dd1>29):
        print('Feb in the year',yyyy1,'can not have more than 29 days')
    elif (yyyy2%4!=0 and mm2==months['Feb'] and dd2>28) or (yyyy2%4==0 and yyyy2%100==0 and yyyy2%400!=0 and mm2==months['Feb'] and dd2>28):
        print('Feb in the year',yyyy2,'can not have more than 28 days')
    elif (yyyy1%4!=0 and mm1==months['Feb'] and dd1>28) or (yyyy1%4==0 and yyyy1%100==0 and yyyy1%400!=0 and mm1==months['Feb'] and dd1>28):
        print('Feb in the year',yyyy1,'can not have more than 28 days')
    elif dd2>=dd1:
        dd=dd2-dd1
        if mm2>=mm1:
            mm=mm2-mm1
            yyyy=yyyy2-yyyy1
            print('The total time is',yyyy,'Years',mm,'Months',dd,'Days')
        else:
            mm2=mm2+12
            mm=mm2-mm1
            yyyy2=yyyy2-1
            yyyy=yyyy2-yyyy1
            print('The total time is',yyyy,'Years',mm,'Months',dd,'Days')
    else:
        dd2=dd2+30
        dd=dd2-dd1
        mm2=mm2-1
        if mm2>=mm1:
            mm=mm2-mm1
            yyyy=yyyy2-yyyy1
            print('The total time is',yyyy,'Years',mm,'Months',dd,'Days')
        else:
            mm2=mm2+12
            mm=mm2-mm1
            yyyy2=yyyy2-1
            yyyy=yyyy2-yyyy1
            print('The total time is',yyyy,'Years',mm,'Months',dd,'Days')
