def add_scalar_and_vector(v,s):
    
    """
    add_scalar_and_vector=>
                input: A list of integers 'v' and an integer 's'.
                output: A list of integers 'r_vector'.
                desc.: The function computes and returns the sum of 'v' + 's'. 
    """

    r_vector=[]
    for i in range(0,len(v)):
        x=v[i]+s
        r_vector.append(x)
        
        

    return r_vector

def add_vectors(v1,v2):
    
    """
    add_vectors=>
                input: Two lists of integers 'v1' and 'v2'.
                output: A list of integers 'r_vector'.
                desc.: The function computes and returns the sum of 'v1' + 'v2'. 
    """
    
    NULL='NULL'
    r_vector=[]

    try:
        mx=max(len(v1),len(v2))
        for i in range(0,mx):
            x=v1[i]+v2[i]
            r_vector.append(x)

        return r_vector
    
    except:
        return  NULL

def sub_vectors(v1,v2):
    
    """
    sub_vectors=>
                input: Two lists of integers 'v1' and 'v2'.
                output: A list of integers 'r_vector'.
                desc.: The function computes and returns the difference of 'v1' - 'v2'. 
    """

    NULL='NULL'
    r_vector=[]

    try:
        mx=max(len(v1),len(v2))

        for i in range(0,mx):
            x=v1[i]-v2[i]
            r_vector.append(x)


        return r_vector
    except:
        return  NULL

def mult_vectors(v1,v2):
    
    """
    mult_vectors=>
                input: Two lists of integers 'v1' and 'v2'.
                output: An integer 'p'.
                desc.: The function computes and returns the product of 'v1' * 'v2'. 
    """

    
    NULL='NULL'
    

    try:
        mx=max(len(v1),len(v2))

        p=0

        for i in range(0,mx):
            p+=v1[i]*v2[i]


        return p
    except:
        return  NULL
    
def sum_vector(v):
    
    """
    sum_vector=>
                input: A list of integers 'v'.
                output: An integer 's'.
                desc.: The function computes and returns the sum of  of the elements of 'v'. 
    """
    
    s=0
    
    for i in range(0,len(v)):
        s+=v[i]
        
    return s

def prod_vector(v):
    
    """
    prod_vector=>
                input: A list of integers 'v'.
                output: An integer 'p'.
                desc.: The function computes and returns the product of the elements of 'v'. 
    """
    
    p=1
    
    for i in range(0,len(v)):
        p*=v[i]
        
    return p

def avg_vector(v):
    
    """
    avg_vector=>
                input: A list of integers 'v'.
                output: An integer == 's' divided by the number of elements of 'v'.
                desc.: The function computes and returns the average of the elements of 'v'. 
    """
    
    s=0
    
    for i in range(0,len(v)):
        s+=v[i]
        
        
    return s/len(v)

def min_vector(v):
    
    """
    min_vector=>
                input: A list of integers 'v'.
                output: An integer 'mn'.
                desc.: The function computes and returns the minimum of the elements of 'v'. 
    """
    
    mn=v[0]
    
    for i in range(1,len(v)):
        if v[i]<mn:
            mn=v[i]
            
    return  mn

def max_vector(v):
    
    """
    max_vector=>
                input: A list of integers 'v'.
                output: An integer 'mx'.
                desc.: The function computes and returns the maximum of the elements of 'v'. 
    """
    
    mx=v[0]
    
    for i in range(1,len(v)):
        if v[i]>mx:
            mx=v[i]
            
    return mx

