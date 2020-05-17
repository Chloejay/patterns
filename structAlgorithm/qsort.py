#! /usr/bin/env python

def quicksort(lst):
    
    if len(lst) <= 1:
        return lst 
    else:
        import random
        pivot= random.choice(lst)
        left, middle,right = [], [], []
        for val in lst:
            if val < pivot:
                left.append(val)
            elif val == pivot:
                middle.append(val) 
            elif val > pivot:
                right.append(val) 
        
        return quicksort(left) + middle + quicksort(right) 


    
if __name__ == '__main__':

    print(quicksort([4,2,10,1]))