def selectsort(lst):
    n= len(lst)
    for i in range(n):
        smallest= i 
        for j in range(i+1, n):
            if lst[j]< lst[smallest]:
                #replace the smallest value to j 
                smallest =j 
        lst[smallest], lst[i]= lst[i], lst[smallest] #swap 
    return lst 


if __name__=='__main__':
    print(selectsort([4,2,10,1])) 

