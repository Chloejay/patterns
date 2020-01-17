def test(val):
    '''
    the function argument val will return its self value two times 
    >>> test('ok')
    okok #get it fall 
    >>> test(2)
    4
    '''
    return val *2 



if __name__=='__main__':
    import doctest
    doctest.testmod() 
