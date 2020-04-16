def insertionsort(lst):
    n= len(lst)
    for i in range(n):
        cur= lst[i]
        pos= i 

        while pos > 0 and lst[pos-1] >cur:
            #shift lst 
            lst[pos]= lst[pos-1]
            pos-=1  

        lst[pos]= cur 

    return lst 


if __name__=='__main__':
    print(insertionsort([4,2,10,1]))