#! /usr/bin/env python

def bubblesort(lst):
    n= len(lst)
    for i in range(n):
        for j in range(n-1):
            if lst[j]> lst[j+1]:
                tmp= lst[j]
                lst[j],lst[j+1]= lst[j+1], tmp #swap 
    return lst 

if __name__=='__main__':
    print(bubblesort([4,2,10,1])) 