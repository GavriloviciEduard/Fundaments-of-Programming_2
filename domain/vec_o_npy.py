import numpy as np


def add_scalar_and_vector_numpy(v,s):
    
    """
    add_scalar_and_vector_numpy=>
                input: A list of integers 'v' and an integer 's'.
                output: A list of integers 'r_vector'.
                desc.: The function computes and returns the sum of 'v' + 's'. 
    """
    
    v=np.array(v)
    
    v=list(v+s)
    
    return v

def add_vectors_numpy(v1,v2):
    
    """
    add_vectors_numpy=>
                input: Two lists of integers 'v1' and 'v2'.
                output: A list of integers.
                desc.: The function computes and returns the sum of 'v1' + 'v2'. 
    """
    
    NULL='NULL'
    
    try:
        
        if len(v1)==len(v2):
        
            v1=np.array(v1)
            v2=np.array(v2)
            return list(np.add(v1,v2))
        
        else:
            return NULL
    
    except:
        return NULL
    
def sub_vectors_numpy(v1,v2):
    
    """
    sub_vectors_numpy=>
                input: Two lists of integers 'v1' and 'v2'.
                output: A list of integers.
                desc.: The function computes and returns the difference of 'v1' - 'v2'. 
    """
    
    NULL='NULL'
    
    try:
        
        if len(v1)==len(v2):
        
            v1=np.array(v1)
            v2=np.array(v2)
            return list(np.subtract(v1,v2))
        
        else:
            return NULL
    
    except:
        return NULL
    
def mult_vectors_numpy(v1,v2):
    
    """
    mult_vectors_numpy=>
                input: Two lists of integers 'v1' and 'v2'.
                output: An integer.
                desc.: The function computes and returns the product of 'v1' * 'v2'. 
    """
    
    NULL='NULL'
    
    try:
        
        v1=np.array(v1)
        v2=np.array(v2)
        
        return np.dot(v1,v2)
    
    except:
        return NULL
    
def sum_vector_numpy(v):
    
    """
    sum_vector_numpy=>
                input: A list of integers 'v'.
                output: An integer.
                desc.: The function computes and returns the sum of  of the elements of 'v'. 
    """
    
    return np.sum(np.array(v))

def prod_vector_numpy(v):
    
    """
    prod_vector_numpy=>
                input: A list of integers 'v'.
                output: An integer.
                desc.: The function computes and returns the product of the elements of 'v'. 
    """
    
    return np.prod(np.array(v))

def avg_vector_numpy(v):
    
    """
    avg_vector_numpy=>
                input: A list of integers 'v'.
                output: An integer.
                desc.: The function computes and returns the average of the elements of 'v'. 
    """
    
    return np.average(np.array(v))


def min_vector_numpy(v):
    
    """
    min_vector_numpy=>
                input: A list of integers 'v'.
                output: An integer.
                desc.: The function computes and returns the minimum of the elements of 'v'. 
    """
    
    return np.amin(np.array(v))

def max_vector_numpy(v):
    
    """
    max_vector_numpy=>
                input: A list of integers 'v'.
                output: An integer.
                desc.: The function computes and returns the maximum of the elements of 'v'. 
    """
    
    return np.amax(np.array(v))
    

