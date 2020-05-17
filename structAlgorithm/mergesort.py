#! /usr/bin/env python

# divide-conquer, merge sort complexity O(n lg n)


def merge(lst1, lst2):
    result = list() 
    i, j = 0, 0
    while i <len(lst1) and j <len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1 
        else:
            result.append(lst2[j])
            j += 1 
    result += lst1[i:]
    result += lst2[j:]

    return result 

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid= int(len(lst)/2)
        # recursive 
        lst1, lst2 = mergesort(lst[:mid]), mergesort(lst[mid:])

    return merge(lst1, lst2) 


      
if __name__ == '__main__':

    lst = [4,2,10,1]
    print(mergesort(lst))